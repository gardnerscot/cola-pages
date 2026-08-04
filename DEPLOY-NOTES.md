# Deploy Notes — cola-pages

**GitHub Pages serves from `main` (branch `main`, path `/`), NOT from `gh-pages`.**

## How to deploy
1. Commit + push to `main`.
2. GitHub Pages auto-rebuilds (usually 1–2 min).
3. Verify: `GET /repos/gardnerscot/cola-pages/pages/builds/latest` → status `built` with your commit SHA, then curl the live URL for HTTP 200.

## Do NOT
- Do NOT use the gh-pages API deployment flow for this repo. The `gh-pages` branch exists but is **legacy/dead** — it was synced from main in older setups and Pages no longer serves it (its tree lacks `guides/` entirely while the live site serves them). Deploying there publishes nothing.
- Do NOT create a new repo for page deploys. Everything lives in `cola-pages` (public, required for Pages).

## Context
- Live root: https://gardnerscot.github.io/cola-pages/
- sitemap.xml and robots.txt live in the repo root and are served as-is.
- Relative paths (`../../product-pages.css`) are required — Pages serves from the repo root path.
