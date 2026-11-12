# jamesfreemanhistorian.com

Source for the site, built with [Quarto](https://quarto.org) and published to GitHub Pages.

## Where things live

| To change | Edit |
|---|---|
| Home page, bio, research themes | `index.qmd` |
| Publications (`featured: true` also shows an entry on the home page) | `publications.yml` |
| Commons chamber chart in the hero | `data/commons-seats.csv` |
| Colours and fonts | `custom.scss` |
| Tools page and its list of tools | `tools/index.qmd` and `tools/tools.yml` |
| A tool, such as plum pudding charts | `tools/<name>/index.html`, a self-contained page that Quarto copies as it is |

The projects gallery and the resources guide are not live yet. Their starter files are in `_starters/`, with instructions in `_starters/README.md`.

## Preview on your computer

1. Install Quarto from https://quarto.org/docs/get-started/
2. `pip install -r requirements.txt`
3. In this folder, run `quarto preview`

## Publish

1. Push this folder to a new public GitHub repo named `<your-username>.github.io`, so that other repos (such as `ecw-sieges-map`) appear under the same domain.
2. In the repo's Settings > Pages, set Source to "GitHub Actions" and enter `jamesfreemanhistorian.com` as the custom domain.
3. Pushing to `main` runs the workflow in `.github/workflows/publish.yml`, which builds the site and publishes it to GitHub Pages.
4. At Porkbun, use Quick DNS Config > GitHub to point the domain at GitHub Pages, then tick Enforce HTTPS in GitHub once the certificate is issued.

## Tools

Each tool is a self-contained page in its own folder under `tools/` (its own styles and code, matching the site's palette and fonts). Quarto doesn't render these pages; `_quarto.yml` lists each folder under `resources`, so it is copied into the built site unchanged. Tools run in the visitor's browser: nothing they paste or open is uploaded or stored.

To add a tool:

1. Put its page at `tools/<name>/index.html`, with a 16:9 `thumb.svg` (or `.png`) beside it.
2. Add `- /tools/<name>/**` under `resources` in `_quarto.yml`.
3. Add an entry to `tools/tools.yml`; it appears as a tile on the Tools page.

### Plum pudding charts

`tools/plum-pudding/` generates coordinates for circular waffle charts for Tableau. Excel files are read with SheetJS, loaded only when needed: the page uses `tools/plum-pudding/xlsx.full.min.js` if that file exists, and otherwise loads SheetJS 0.20.3 from the official CDN. To self-host it, download `https://cdn.sheetjs.com/xlsx-0.20.3/package/dist/xlsx.full.min.js` into `tools/plum-pudding/`. Use the cdn.sheetjs.com build, not the `xlsx` package on npm, which is an older version missing security fixes.
