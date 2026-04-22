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

## Cloudflare Pages Deployment

Use Cloudflare Pages Git integration against this repository.

### Required settings

- Framework preset: `None`
- Build command: `pip install -r requirements.txt && mkdocs build`
- Build output directory: `site`
- Root directory: repository root
- Python version environment variable: `PYTHON_VERSION=3.12`

### GitHub Action deployment (included)

This repository also includes [cloudflare-pages.yml](.github/workflows/cloudflare-pages.yml), which will:

- install dependencies
- build the MkDocs site
- deploy `site/` to Cloudflare Pages project `tfl-doc-migration-test`

Add these repository secrets before enabling the workflow:

- `CLOUDFLARE_API_TOKEN`
- `CLOUDFLARE_ACCOUNT_ID`

### Custom domain

1. In Cloudflare Pages, open your project.
2. Go to `Custom domains`.
3. Add `aidanstew.art`.
4. Follow Cloudflare DNS prompts (usually CNAME flattening or managed records if domain is already in Cloudflare).

After DNS propagation, every push to the default branch will rebuild and redeploy.

## Notes on Rich Media

- Mermaid: wrapped in Markdown pages using fenced `mermaid` blocks.
- PDFs: wrapped with `<object>` embeds and download fallback links.
- STLs: wrapped using `<model-viewer>` for interactive viewing.
- Spreadsheets: wrapper pages can render tables using `read_excel` or `read_csv`.
