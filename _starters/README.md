# Starter files for sections not yet on the site

Quarto ignores any folder whose name starts with an underscore, so nothing here is published.
Each file is ready to copy into place when you want that section to go live.

| Section | Copy | To |
|---|---|---|
| Data and politics page (project gallery) | `_starters/data.qmd` | `data.qmd` |
| A project built in this repo (worked example) | `_starters/projects/election-turnout/` and `_starters/data/turnout.csv` | `projects/election-turnout/` and `data/turnout.csv` |
| Projects kept in their own repos | `_starters/external-projects.yml` and `_starters/images/sieges-thumb.svg` | `external-projects.yml` and `images/sieges-thumb.svg` |
| Projects band on the home page | `_starters/home-projects-section.md` | follow the steps in its comment |
| Resources guide | `_starters/resources.qmd` | `resources.qmd` |

Then add the page to the menu in `_quarto.yml`, under `navbar:` > `left:`:

```yaml
      - href: data.qmd
        text: Data and politics
      - href: resources.qmd
        text: Resources
```
