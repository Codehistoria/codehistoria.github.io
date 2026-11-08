<!--
Projects band for the home page. To switch it on:
1. Add this listing to the `listing:` list at the top of index.qmd (under featured-articles):

  - id: featured-projects
    contents:
      - projects/*/index.qmd
      - external-projects.yml
    sort: "date desc"
    max-items: 2
    template: _templates/projects.ejs

2. Paste everything below this comment into index.qmd, just above the About band
   (the line that starts ":::: {.wrap .about #about}" sits inside it).
-->

::::: {.band .band-tint}

:::: {.wrap}

::: {.section-head}

## Projects
[All projects](data.qmd)

:::

::: {#featured-projects}

:::

::::

:::::

