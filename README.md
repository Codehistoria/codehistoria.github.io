# jamesfreemanhistorian.com

Source for the site, built with [Quarto](https://quarto.org) and published to GitHub Pages.

## Where things live

| To change | Edit |
|---|---|
| Home page, bio, research themes | `index.qmd` |
| Publications (`featured: true` also shows an entry on the home page) | `publications.yml` |
| Commons chamber chart in the hero | `data/commons-seats.csv` |
| Colours and fonts | `custom.scss` |

The projects gallery and the resources guide are not live yet. Their starter files are in `_starters/`, with instructions in `_starters/README.md`.

## Preview on your computer

1. Install Quarto from https://quarto.org/docs/get-started/
2. `pip install -r requirements.txt`
3. In this folder, run `quarto preview`

## Publish

1. Push this folder to a new public GitHub repo named `<your-username>.github.io`, so that other repos (such as `ecw-sieges-map`) appear under the same domain.
2. Pushing to `main` runs the workflow in `.github/workflows/publish.yml`, which builds the site into a `gh-pages` branch.
3. In the repo's Settings > Pages, set the source to the `gh-pages` branch and enter `jamesfreemanhistorian.com` as the custom domain.
4. At Porkbun, use Quick DNS Config > GitHub to point the domain at GitHub Pages, then tick Enforce HTTPS in GitHub once the certificate is issued.
