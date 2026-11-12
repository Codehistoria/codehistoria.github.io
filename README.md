# jamesfreemanhistorian.com

Source for the site, built with [Quarto](https://quarto.org) and published to GitHub Pages.

## Where things live

| To change | Edit |
|---|---|
| Home page, bio, research themes | `index.qmd` |
| Publications (`featured: true` also shows an entry on the home page) | `publications.yml` |
| Commons chamber chart in the hero | `data/commons-seats.csv` |
| Colours and fonts | `custom.scss` |
| Plum pudding chart tool (served at `/plum-pudding/`) | `plum-pudding/index.html`, a self-contained page that Quarto copies as it is |

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

## Plum pudding chart tool

`plum-pudding/index.html` is a standalone page (its own styles and code, matching the site's palette and fonts). Quarto doesn't render it; `_quarto.yml` lists it under `resources`, so it is copied into the built site unchanged. Everything in it runs in the visitor's browser: pasted data and opened Excel or CSV files are never uploaded or stored.

Excel files are read with SheetJS, loaded only when needed. The page uses `plum-pudding/xlsx.full.min.js` if that file exists, and otherwise loads SheetJS 0.20.3 from the official CDN. To self-host it, download `https://cdn.sheetjs.com/xlsx-0.20.3/package/dist/xlsx.full.min.js` into `plum-pudding/`. Use the cdn.sheetjs.com build, not the `xlsx` package on npm, which is an older version missing security fixes.
