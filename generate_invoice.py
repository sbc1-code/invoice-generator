#!/usr/bin/env python3
"""
Invoice Generator (EN/ES)
Generates professional HTML invoices with language toggle support.

Usage:
    python3 generate_invoice.py --invoice-number INV-001 --date 2026-03-01 --period "March 1-31, 2026" --due-date 2026-03-15
    python3 generate_invoice.py --invoice-number INV-002 --date 2026-04-01 --period "April 1-30, 2026" --due-date 2026-04-15 --amount 2500 --lang es
"""
import argparse
from pathlib import Path


LABELS = {
    "en": {
        "title": "Invoice",
        "date": "Date",
        "invoice_num": "Invoice #",
        "bill_to": "Bill To",
        "terms": "Terms",
        "due_date": "Due Date",
        "th_date": "Date",
        "th_desc": "Description",
        "th_qty": "Qty",
        "th_rate": "Rate",
        "th_amount": "Amount",
        "desc_title": "Professional Consulting Services",
        "service_intro": "Professional consulting services including:",
        "bullet1": "Analysis and reporting",
        "bullet2": "Project management",
        "bullet3": "Technical support",
        "bullet4": "Documentation and deliverables",
        "service_period": "Service Period",
        "contract_ref": "Contract Reference: Service Agreement",
        "wire_details": "Wire Transfer Details:",
        "bank": "Bank",
        "account_holder": "Account Holder",
        "account_num": "Account #",
        "email": "Email",
        "subtotal": "Subtotal",
        "amount_due": "Amount Due (USD)",
    },
    "es": {
        "title": "Factura",
        "date": "Fecha",
        "invoice_num": "Factura #",
        "bill_to": "Facturar a",
        "terms": "Terminos",
        "due_date": "Fecha Limite",
        "th_date": "Fecha",
        "th_desc": "Descripcion",
        "th_qty": "Cantidad",
        "th_rate": "Tarifa",
        "th_amount": "Monto",
        "desc_title": "Servicios Profesionales de Consultoria",
        "service_intro": "Servicios profesionales de consultoria incluyendo:",
        "bullet1": "Analisis y reporte",
        "bullet2": "Gestion de proyecto",
        "bullet3": "Soporte tecnico",
        "bullet4": "Documentacion y entregables",
        "service_period": "Periodo de servicio",
        "contract_ref": "Referencia: Acuerdo de Servicio",
        "wire_details": "Datos Bancarios:",
        "bank": "Banco",
        "account_holder": "Titular",
        "account_num": "No. de Cuenta",
        "email": "Correo",
        "subtotal": "Subtotal",
        "amount_due": "Saldo (USD)",
    },
}


def generate_invoice(invoice_number, date, amount, quantity, period, due_date, lang="en"):
    L = LABELS[lang]
    total = amount * quantity
    amount_fmt = f"${amount:,.2f}"
    total_fmt = f"${total:,.2f}"
    qty_fmt = str(int(quantity)) if quantity == int(quantity) else str(quantity)

    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{L['title']} {invoice_number}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            color: #333;
            line-height: 1.4;
            font-size: 12px;
        }}
        @page {{
            size: A4;
            margin: 0.5in;
        }}
        .invoice-container {{
            width: 100%;
            max-width: none;
            margin: 0;
            background: white;
            border: 2px solid #000;
            page-break-inside: avoid;
        }}
        .header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            padding: 15px;
            border-bottom: 2px solid #000;
        }}
        .company-info {{
            flex: 1;
        }}
        .company-name {{
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        .company-details {{
            font-size: 14px;
            line-height: 1.3;
        }}
        .invoice-title {{
            flex: 1;
            text-align: right;
        }}
        .invoice-title h1 {{
            font-size: 36px;
            margin: 0;
            font-weight: bold;
        }}
        .invoice-meta {{
            display: flex;
            gap: 20px;
            margin-top: 10px;
        }}
        .meta-box {{
            border: 2px solid #000;
            padding: 8px 12px;
            text-align: center;
            min-width: 80px;
        }}
        .meta-label {{
            font-weight: bold;
            font-size: 14px;
        }}
        .meta-value {{
            font-size: 14px;
            margin-top: 2px;
        }}
        .bill-to-section {{
            padding: 20px;
            border-bottom: 2px solid #000;
        }}
        .bill-to-header {{
            background: #000;
            color: white;
            padding: 8px 12px;
            font-weight: bold;
            margin-bottom: 10px;
            display: inline-block;
        }}
        .bill-to-content {{
            border: 2px solid #000;
            padding: 15px;
            font-size: 14px;
            line-height: 1.4;
        }}
        .terms-section {{
            display: flex;
            justify-content: flex-end;
            padding: 0 20px;
            margin-bottom: 20px;
        }}
        .terms-box {{
            display: flex;
            border: 2px solid #000;
        }}
        .terms-label, .due-date-label {{
            background: #f0f0f0;
            padding: 8px 12px;
            font-weight: bold;
            border-right: 2px solid #000;
            text-align: center;
        }}
        .terms-value, .due-date-value {{
            padding: 8px 12px;
            text-align: center;
            min-width: 100px;
        }}
        .items-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 0 20px 20px 20px;
            width: calc(100% - 40px);
        }}
        .items-table th {{
            background: #f0f0f0;
            border: 2px solid #000;
            padding: 10px;
            text-align: center;
            font-weight: bold;
        }}
        .items-table td {{
            border: 2px solid #000;
            padding: 10px;
            vertical-align: top;
        }}
        .description-cell {{
            text-align: left;
            width: 50%;
        }}
        .number-cell {{
            text-align: center;
            width: 12.5%;
        }}
        .amount-cell {{
            text-align: right;
            width: 12.5%;
        }}
        .totals-section {{
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            padding: 20px;
        }}
        .payment-info {{
            flex: 1;
            font-size: 16px;
            font-weight: bold;
        }}
        .totals-table {{
            border-collapse: collapse;
        }}
        .totals-table td {{
            border: 2px solid #000;
            padding: 8px 15px;
            font-size: 16px;
        }}
        .totals-label {{
            background: #f0f0f0;
            font-weight: bold;
            text-align: center;
        }}
        .totals-amount {{
            text-align: right;
            min-width: 120px;
        }}
        .balance-due {{
            font-weight: bold;
            font-size: 18px;
        }}
        .banking-details {{
            margin-top: 10px;
            font-size: 14px;
            line-height: 1.3;
        }}
        @media print {{
            body {{ margin: 0; padding: 10px; }}
            .invoice-container {{ border: 1px solid #000; }}
        }}
    </style>
</head>
<body>
    <div class="invoice-container">
        <div class="header">
            <div class="company-info">
                <div class="company-name">YOUR NAME HERE</div>
                <div class="company-details">
                    Digital Services &amp; Consulting<br>
                    123 Main Street, Suite A<br>
                    City, State 12345<br>
                    Ph. (555) 000-0000<br>
                    Tax ID: XXXXXXXXXXX
                </div>
            </div>
            <div class="invoice-title">
                <h1>{L['title']}</h1>
                <div class="invoice-meta">
                    <div class="meta-box">
                        <div class="meta-label">{L['date']}</div>
                        <div class="meta-value">{date}</div>
                    </div>
                    <div class="meta-box">
                        <div class="meta-label">{L['invoice_num']}</div>
                        <div class="meta-value">{invoice_number}</div>
                    </div>
                </div>
            </div>
        </div>

        <div class="bill-to-section">
            <div class="bill-to-header">{L['bill_to']}</div>
            <div class="bill-to-content">
                Client Corp<br>
                456 Business Avenue, Suite B1<br>
                City, State 00000<br>
                Tax ID: XXXXXXXXXXX
            </div>
        </div>

        <div class="terms-section">
            <div class="terms-box">
                <div class="terms-label">{L['terms']}</div>
                <div class="terms-value">Net 15</div>
                <div class="due-date-label">{L['due_date']}</div>
                <div class="due-date-value">{due_date}</div>
            </div>
        </div>

        <table class="items-table">
            <thead>
                <tr>
                    <th>{L['th_date']}</th>
                    <th>{L['th_desc']}</th>
                    <th>{L['th_qty']}</th>
                    <th>{L['th_rate']}</th>
                    <th>{L['th_amount']}</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="number-cell">{date}</td>
                    <td class="description-cell">
                        <strong>{L['desc_title']} | {period}</strong><br><br>

                        {L['service_intro']}<br><br>

                        &bull; {L['bullet1']}<br>
                        &bull; {L['bullet2']}<br>
                        &bull; {L['bullet3']}<br>
                        &bull; {L['bullet4']}<br><br>

                        <em>{L['service_period']}: {period}</em><br>
                        <em>{L['contract_ref']}</em>
                    </td>
                    <td class="number-cell">{qty_fmt}</td>
                    <td class="amount-cell">{amount_fmt}</td>
                    <td class="amount-cell">{total_fmt}</td>
                </tr>
            </tbody>
        </table>

        <div class="totals-section">
            <div class="payment-info">
                <strong>{L['wire_details']}</strong>
                <div class="banking-details">
                    {L['bank']}: Example Bank<br>
                    {L['account_holder']}: Your Name<br>
                    {L['account_num']}: XXXX-XXXX-XXXX<br>
                    Routing #: XXXXXXXXX<br>
                    Swift: XXXXXXXXX<br><br>
                    {L['email']}: you@example.com
                </div>
            </div>
            <table class="totals-table">
                <tr>
                    <td class="totals-label">{L['subtotal']}</td>
                    <td class="totals-amount">{total_fmt}</td>
                </tr>
                <tr>
                    <td class="totals-label">{L['amount_due']}</td>
                    <td class="totals-amount balance-due">{total_fmt}</td>
                </tr>
            </table>
        </div>
    </div>
</body>
</html>"""

    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / f"{invoice_number}.html"
    output_path.write_text(html)
    print(f"Invoice generated: {output_path}")
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Generate HTML invoice")
    parser.add_argument("--invoice-number", required=True, help="e.g. INV-001")
    parser.add_argument("--date", required=True, help="Invoice date, e.g. 3/1/2026")
    parser.add_argument("--amount", type=float, default=1500.00, help="Rate per unit (default: 1500)")
    parser.add_argument("--quantity", type=float, default=1, help="Quantity (default: 1)")
    parser.add_argument("--period", required=True, help='e.g. "March 1-31, 2026"')
    parser.add_argument("--due-date", required=True, help="e.g. 3/15/2026")
    parser.add_argument("--lang", choices=["en", "es"], default="en", help="Invoice language (default: en)")
    args = parser.parse_args()

    generate_invoice(
        invoice_number=args.invoice_number,
        date=args.date,
        amount=args.amount,
        quantity=args.quantity,
        period=args.period,
        due_date=args.due_date,
        lang=args.lang,
    )


if __name__ == "__main__":
    main()
