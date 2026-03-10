# Bilingual Invoice Generator (EN/ES)

CLI tool that generates professional, print-ready HTML invoices in both English and Spanish. Built for cross-border consulting engagements.

## Features

- Bilingual layout (EN/ES) on every field: headers, labels, descriptions, payment terms
- Print-optimized A4 format with clean borders and structured sections
- CLI interface with configurable amount, quantity, period, and due date
- Self-contained HTML output (no external dependencies for the invoice itself)
- Wire transfer / banking details section
- Factura numbering system

## Usage

```bash
python3 generate_invoice.py \
  --invoice-number INV-001 \
  --date "3/1/2026" \
  --period "March 1-31, 2026" \
  --due-date "3/15/2026"
```

With custom amount:

```bash
python3 generate_invoice.py \
  --invoice-number INV-002 \
  --date "4/1/2026" \
  --amount 2500 \
  --quantity 1 \
  --period "April 1-30, 2026" \
  --due-date "4/15/2026"
```

Output: `./output/INV-001.html`

Open the HTML file in a browser and print to PDF for a clean, professional invoice.

## Customization

Edit the HTML template inside `generate_invoice.py` to update:

- Your name and address (header section)
- Client billing info (bill-to section)
- Banking / wire transfer details (totals section)
- Line item descriptions
- RFC / tax ID numbers

## Requirements

- Python 3.8+ (no external packages needed, uses only `argparse` and `pathlib`)

## License

MIT
