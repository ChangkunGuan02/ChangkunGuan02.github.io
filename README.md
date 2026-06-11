# changkunguan02.github.io

Personal academic website of **Changkun Guan** — Ph.D. student in Operations Research at Georgia Tech ISyE.

Live at [changkunguan02.github.io](https://changkunguan02.github.io), built with [Jekyll](https://jekyllrb.com/) and the [AcademicPages](https://github.com/academicpages/academicpages.github.io) theme (MIT License, see LICENSE), hosted on GitHub Pages.

## Editing content

| Content | Where |
|---|---|
| Home / About | `_pages/about.md` |
| Publications | `_publications/*.md` (one file per paper) |
| Research projects | `_portfolio/*.md` |
| Talks | `_talks/*.md` |
| Teaching | `_teaching/*.md` |
| CV (web) | `_pages/cv.md` |
| CV (PDF) | `files/cv.pdf` |
| Sidebar profile & links | `author:` section of `_config.yml` |
| Navigation | `_data/navigation.yml` |

To replace the placeholder monogram avatar with a photo: add `images/profile.jpg` and set `avatar: "profile.jpg"` in `_config.yml`.

## Local development

```bash
bundle install
bundle exec jekyll serve
```

Then open <http://localhost:4000>. Pushing to `main` deploys automatically via GitHub Pages.
