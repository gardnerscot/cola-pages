# OUTLINE — The Definitive Free SEO Guide (no-budget edition)

**Status:** Draft outline — for building/upgrading `guides/free-seo-tools/index.html`
**Wedge:** The gap between free Google Search Console and $129/mo enterprise tools is ours to own.
**CTA:** LifeCapture = the automated version of this workflow.

---

## Positioning & Title

**The narrative to own:** Ahrefs charges $129/mo to tell you what Google will tell you for free — if you know where to look. Solopreneurs use maybe 5% of those tools' features. The data that actually matters (what people searched, what you rank for, what to fix) is free. This guide is the bridge between "free GSC" and "$129/mo" — no credit card, no trial, no expiry.

**Title options:**
- A: "The Free SEO Stack: Rank Without Paying $129/Month" ← lead
- B: "Free SEO for Bootstrapped Founders: The Definitive Guide"
- C: "SEO Without the Subscription: The Free Guide That Actually Works"

**Meta:**
- Page title: `Free SEO Tools That Actually Work: The No-Budget Guide (2026)`
- Meta description: `Rank without paying $129/month. Keyword research, on-page basics, and one weekly habit — all free. No credit card required.`

---

## The 3-Part Arc (the tip's skeleton, expanded)

### Part 1 — Keyword Idea (no keyword tool required)
- **The GSC goldmine:** your Queries report is real demand data (impressions, clicks, CTR, position) — the one thing no paid tool has for *your* site
- **Free demand discovery:** Google autocomplete, People Also Ask, "searches related to" — Google does the market research for you
- **Competitor recon with `site:`** — no subscription needed
- **Free-tier keyword tools:** Google Keyword Planner, Ubersuggest free, AnswerThePublic free — what they're actually good for
- **The discipline:** pick ONE keyword this week. Not ten. One.
- 💡 ADHD/personal-organization nod: a keyword list that lives somewhere retrievable (guess where) beats a folder of 14 bookmarks

### Part 2 — On-Page Basics
- **Title tag formula:** one keyword + one benefit, ≤60 chars
- **Meta description:** the free CTR lever (write the ad, get the click)
- **H1/H2 hierarchy:** one idea per page, structured so a skimmer gets it
- **Content depth that answers completely** — the query's job description, not a word count
- **Internal linking:** the free rank lever nobody uses (link your own pages like Ahrefs links its blog)
- **E-E-A-T signals:** author line, About page, freshness — free trust
- **Core Web Vitals:** PageSpeed Insights + GSC's CWV report — speed data, $0
- **Schema basics:** Article/FAQ via free validators

### Part 3 — One Weekly Habit (the 30-minute loop)
- **The loop:** open GSC → find the page closest to page 1 → improve that one page → done for the week
- **90-day compounding:** 12 small wins beat one panic overhaul
- **What NOT to do:** don't buy the $129/mo FOMO, don't chase keywords you can't win, don't trust the "5,000 keyword ideas" export
- 💡 ADHD-friendly framing: a small consistent loop > a big annual push (and this is exactly the "capture, review, act" rhythm LifeCapture is built for)

---

## CTA Section — "The automated version"

- **Hook:** this whole workflow — capturing keyword ideas, keeping the weekly checklist, finding that note you wrote three weeks ago — has a manual version and an automated version
- **The manual version:** 47 tabs, a Notes app graveyard, a bookmark folder named "seo stuff"
- **The automated version:** LifeCapture — capture a keyword idea from anywhere (type, screenshot, voice), file it in a bucket, retrieve it when you sit down to write
- **Tie to real features:** quick capture, buckets, smart search — no invented claims
- **CTA button:** `Try LifeCapture` → `/lifecapture/`

---

## SEO Targeting (steal Ahrefs traffic)

**Primary clusters:**
- `free seo tools` / `free seo tools for beginners`
- `ahrefs alternative free` / `how to do seo without ahrefs` / `is ahrefs worth it`
- `free keyword research tools` / `google search console guide`
- `seo tools for solopreneurs` / `seo for indie hackers`

**Notes:**
- Existing page already carries `free seo tools` in H1 + sitemap — this upgrade defends and expands that
- Internal links in: from `lifecapture/`, `talkboard/free-seo-guide.html`, `guides/best-life-capture-app/`
- FAQ section doubles as a People-Also-Ask capture net

---

## Build Checklist (when greenlit)

1. Rewrite `guides/free-seo-tools/index.html` (current: 10KB, thin) using `product-pages.css`
2. H1 = chosen title; wedge line above the fold; CTA button above the fold + final CTA at bottom
3. Three parts as H2 sections, one idea per section (copywriting rule: clarity > cleverness)
4. FAQ block (4-6 questions pulled from People Also Ask)
5. "More from SG1 Labs" footer (existing pattern) + link to `lifecapture/`
6. Keep sitemap URL; add to `robots.txt`-visible structure; no new sitemap entry needed if URL unchanged
7. Deploy to gh-pages (existing flow, commit + push)

---

## Open questions for Scot
- **Replace or sibling?** Upgrade the existing `free-seo-tools` page (keeps the URL/backlinks) — my recommendation — or new page + redirect?
- **FrugalSEO tie-in:** cross-link to `frugalseo.shipdrop.dev` (already linked on the page) or keep this guide standalone?
