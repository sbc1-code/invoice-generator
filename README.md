# Invoice Generator

Bilingual invoice generator for cross-border consulting.

**[Live Demo](https://sbc1-code.github.io/invoice-generator/)**

## What it does

- Interactive browser-based invoice generator with live preview
- Bilingual EN/ES layout on every field: headers, labels, descriptions, payment terms
- Fill in your details, see the invoice update in real time, then print or save as PDF
- Print-optimized A4 format with clean borders and structured sections

The Python CLI version (`generate_invoice.py`) is also included for automation and scripting.

## CLI Usage

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

## License

MIT
