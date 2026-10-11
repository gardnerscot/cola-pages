#!/usr/bin/env python3
"""SG1 Labs product-page drift auditor.

Compares three layers that must agree:
  1. products/index.html (the hub — source of truth for live products)
  2. go.sg1-labs.us/<slug> redirect worker (final URL must match the hub link)
  3. sg1-labs.us WordPress home page (must feature live products)

Usage:  python3 audit_products.py [--json PATH]
Exit 0 = no drift, exit 1 = drift found. Report printed to stdout.
"""
import json
import re
import subprocess
import sys
import urllib.parse
from pathlib import Path

HUB = Path(__file__).resolve().parent.parent / "products" / "index.html"
UA = "sg1-audit/1.0"
TIMEOUT = 20

# slugs on go.sg1-labs.us that are expected to differ from the hub row link,
# or map outside cola-pages (worker-owned short links we accept as-is)
KNOWN_EXTERNAL = {
    "trialguard": "https://go.sg1-labs.us/trialguard",
    "slopclean": "https://go.sg1-labs.us/slopclean",
    "shipdrop": "https://shipdrop.dev",
    "vibecheck": "https://vibecheck.shipdrop.dev",
    "frugalseo": "https://frugalseo.shipdrop.dev",
}

def sh_curl(url, head=False):
    args = ["curl", "-sgL", "--max-time", str(TIMEOUT), "-A", UA,
            "-o", "/dev/null", "-w", "%{http_code}|%{url_effective}", url]
    if head:
        args.insert(2, "-I")
    out = subprocess.run(args, capture_output=True, text=True, timeout=TIMEOUT + 10).stdout
    code, _, final = out.partition("|")
    return code, final

# hub display names whose go.* slug differs from the naive lowercased name
SLUG_OVERRIDES = {
    "Trial Guard": "trialguard",
}

def parse_hub():
    """Return [{slug, name, status, link}] from products/index.html rows."""
    html = HUB.read_text(encoding="utf-8")
    rows = []
    for m in re.finditer(r'<article class="product-row">.*?</article>', html, re.S):
        row = m.group(0)
        name_m = re.search(r"<h3>([^<]+?)\s*<span", row) or re.search(r"<h3>([^<]+)</h3>", row)
        status = "live" if 'class="status live"' in row else ("soon" if "status soon" in row else "other")
        link_m = re.search(r'class="product-link" href="([^"]+)"', row)
        if not (name_m and link_m):
            continue
        name = name_m.group(1).strip()
        link = link_m.group(1)
        slug = re.search(r"\.\./([a-z0-9-]+)/", link)
        slug = slug.group(1) if slug else SLUG_OVERRIDES.get(name, name.lower().replace(" ", "-"))
        rows.append({"slug": slug, "name": name, "status": status, "link": link})
    return rows

def check_routes(products):
    drift = []
    for p in products:
        if p["status"] != "live":
            continue
        slug = p["slug"]
        code, final = sh_curl(f"https://go.sg1-labs.us/{slug}")
        if code != "200":
            drift.append({"kind": "route_error", "slug": slug,
                          "detail": f"go.sg1-labs.us/{slug} returned HTTP {code}"})
            continue
        # expected final: hub link resolved (relative links resolve onto cola-pages)
        expected = p["link"]
        if not expected.startswith("http"):
            expected = urllib.parse.urljoin("https://gardnerscot.github.io/cola-pages/products/", expected)
        if "cola-dispatch.marswave-543.workers.dev" in final:
            drift.append({"kind": "route_handout", "slug": slug,
                          "detail": f"go.sg1-labs.us/{slug} lands on the STALE handout worker page, hub says {expected}"})
        elif not expected.startswith("https://go.sg1-labs.us/") and final.rstrip("/") != expected.rstrip("/"):
            drift.append({"kind": "route_mismatch", "slug": slug,
                          "detail": f"go.sg1-labs.us/{slug} lands on {final}, hub says {expected}"})
    return drift

def check_wp_home(products):
    drift = []
    out = subprocess.run(["curl", "-sg", "--max-time", str(TIMEOUT), "https://sg1-labs.us/"],
                         capture_output=True, text=True, timeout=TIMEOUT + 10).stdout
    required_on_home = {"OmniChat", "OllamaChat", "USBControl"}
    for name in sorted(required_on_home):
        if f"<h3>{name}</h3>" not in out:
            drift.append({"kind": "wp_missing_card", "slug": name.lower().replace(" ", "-"),
                          "detail": f"flagship product '{name}' has no card on sg1-labs.us home"})
    return drift

def check_detail_pages(products):
    drift = []
    base = HUB.parent.parent
    for p in products:
        if p["status"] != "live" or not p["link"].startswith("../"):
            continue
        page = base / p["slug"] / "index.html"
        if not page.exists():
            drift.append({"kind": "detail_missing", "slug": p["slug"],
                          "detail": f"{p['slug']}/index.html does not exist in cola-pages"})
    return drift

def main():
    products = parse_hub()
    live = [p["name"] for p in products if p["status"] == "live"]
    print(f"Hub: {len(products)} products, {len(live)} live: {', '.join(live)}\n")
    drift = check_routes(products) + check_wp_home(products) + check_detail_pages(products)
    if drift:
        print(f"DRIFT ({len(drift)}):")
        for d in drift:
            print(f"  [{d['kind']}] {d['slug']}: {d['detail']}")
        if "--json" in sys.argv:
            Path(sys.argv[sys.argv.index("--json") + 1]).write_text(json.dumps(drift, indent=1))
        sys.exit(1)
    print("No drift. Routes, hub, and home page agree.")

if __name__ == "__main__":
    main()
