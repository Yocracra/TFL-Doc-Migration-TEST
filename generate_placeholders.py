import os
import glob
from urllib.parse import quote

docs_dir = 'docs'

# Find all media files
mmd_files = glob.glob(f'{docs_dir}/**/*.mmd', recursive=True)
pdf_files = glob.glob(f'{docs_dir}/**/*.pdf', recursive=True)
stl_files = glob.glob(f'{docs_dir}/**/*.stl', recursive=True)
xlsx_files = glob.glob(f'{docs_dir}/**/*.xlsx', recursive=True)
csv_files = glob.glob(f'{docs_dir}/**/*.csv', recursive=True)

generated = {
    'mmd': 0,
    'pdf': 0,
    'stl': 0,
    'xlsx': 0,
    'csv': 0,
    'skipped': 0,
}

# Generate wrapper for .mmd
for f in mmd_files:
    base = os.path.splitext(f)[0]
    md_file = f"{base}.md"
    if os.path.exists(md_file):
        generated['skipped'] += 1
        continue
    name = os.path.basename(base)
    with open(f, 'r') as source:
        content = source.read()
    with open(md_file, 'w') as target:
        target.write(f"# {name}\n\n```mermaid\n{content}\n```\n")
    generated['mmd'] += 1

# Generate wrapper for .pdf
for f in pdf_files:
    base = os.path.splitext(f)[0]
    md_file = f"{base}.md"
    if os.path.exists(md_file):
        generated['skipped'] += 1
        continue
    filename = os.path.basename(f)
    name = os.path.splitext(filename)[0]
    url_encoded_path = quote(filename)
    with open(md_file, 'w') as target:
        target.write(f"# {name}\n\n<object data=\"{url_encoded_path}\" type=\"application/pdf\" width=\"100%\" height=\"800px\">\n  <p>Unable to display PDF file. <a href=\"{url_encoded_path}\">Download</a> instead.</p>\n</object>\n")
    generated['pdf'] += 1

# Generate wrapper for .stl
for f in stl_files:
    base = os.path.splitext(f)[0]
    md_file = f"{base}.md"
    if os.path.exists(md_file):
        generated['skipped'] += 1
        continue
    filename = os.path.basename(f)
    name = os.path.splitext(filename)[0].replace('_', ' ').title()
    url_encoded_path = quote(filename)
    with open(md_file, 'w') as target:
        target.write(f"# {name}\n\n<model-viewer src=\"{url_encoded_path}\" auto-rotate camera-controls style=\"width: 100%; height: 500px; background-color: #2F333D;\"></model-viewer>\n")
    generated['stl'] += 1

# Generate wrapper for .xlsx
for f in xlsx_files:
    base = os.path.splitext(f)[0]
    md_file = f"{base}.md"
    if os.path.exists(md_file):
        generated['skipped'] += 1
        continue
    filename = os.path.basename(f)
    name = os.path.splitext(filename)[0]
    url_encoded_path = quote(filename)
    with open(md_file, 'w') as target:
        target.write(
            f"# {name}\n\n"
            f"{{{{ read_excel('{filename}', sheet_name=0) }}}}\n\n"
            f"[Download source spreadsheet]({url_encoded_path})\n"
        )
    generated['xlsx'] += 1

# Generate wrapper for .csv
for f in csv_files:
    base = os.path.splitext(f)[0]
    md_file = f"{base}.md"
    if os.path.exists(md_file):
        generated['skipped'] += 1
        continue
    filename = os.path.basename(f)
    name = os.path.splitext(filename)[0]
    url_encoded_path = quote(filename)
    with open(md_file, 'w') as target:
        target.write(
            f"# {name}\n\n"
            f"{{{{ read_csv('{filename}') }}}}\n\n"
            f"[Download source CSV]({url_encoded_path})\n"
        )
    generated['csv'] += 1

print(
    "Generated wrappers: "
    f"{generated['mmd']} mmd, "
    f"{generated['pdf']} pdf, "
    f"{generated['stl']} stl, "
    f"{generated['xlsx']} xlsx, "
    f"{generated['csv']} csv; "
    f"skipped {generated['skipped']} existing files."
)
