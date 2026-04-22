# TAMU Fab Lab Docs Site

This repository is configured as a portable MkDocs project that runs the same way on any machine using Docker Compose.

## Stack

- MkDocs
- Material for MkDocs
- Mermaid diagram rendering
- PDF embedding with HTML object tags
- STL embedding with model-viewer
- Spreadsheet rendering with mkdocs-table-reader-plugin

## Local Development (Docker Compose)

Build and serve docs locally:

```bash
docker compose up --build docs
```

Then open `http://localhost:8000`.

Create static site output in `site/`:

```bash
docker compose --profile build run --rm build
```

Regenerate media placeholder pages for `.mmd`, `.pdf`, `.stl`, `.xlsx`, and `.csv` files:

```bash
docker compose --profile tools run --rm placeholders
```

## GitHub Pages Deployment (Recommended)

This repository includes a GitHub Pages workflow:

- [.github/workflows/github-pages.yml](.github/workflows/github-pages.yml)

It builds MkDocs and deploys the generated `site/` directory automatically on push to `main` or `master`.

### One-time GitHub setup

1. In GitHub, open repository `Settings`.
2. Go to `Pages`.
3. Under `Build and deployment`, set `Source` to `GitHub Actions`.
4. Ensure `Custom domain` is empty in `Settings > Pages`.
5. Push to `main` or `master` (or run the workflow manually from `Actions`).

### GitHub Pages URL

After deployment, your site URL will be:

- Project site: `https://<your-github-username>.github.io/TFL-Doc-Migration-TEST/`

If the repository is renamed to `<your-github-username>.github.io`, the site URL becomes:

- User site: `https://<your-github-username>.github.io/`

### Troubleshooting: Plain Page or 404s

If the site looks like a plain HTML page or document links return 404, GitHub is usually serving a branch build instead of the Actions artifact.

Check these in order:

1. In `Settings > Pages`, `Source` must be `GitHub Actions`.
2. In `Actions`, the workflow `Deploy Docs To GitHub Pages` must complete successfully.
3. In `Settings > Pages`, make sure `Custom domain` is empty when using the default GitHub domain.
4. Wait 1-2 minutes after a successful deploy and hard-refresh your browser.

If needed, trigger a clean redeploy from `Actions` by running `Deploy Docs To GitHub Pages` manually.

## Notes on Rich Media

- Mermaid: wrapped in Markdown pages using fenced `mermaid` blocks.
- PDFs: wrapped with `<object>` embeds and download fallback links.
- STLs: wrapped using `<model-viewer>` for interactive viewing.
- Spreadsheets: wrapper pages can render tables using `read_excel` or `read_csv`.
