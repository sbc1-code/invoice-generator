#!/usr/bin/env python3
"""
Bilingual Invoice Generator (EN/ES)
Generates professional HTML invoices for cross-border consulting engagements.

Usage:
    python3 generate_invoice.py --invoice-number INV-001 --date 2026-03-01 --period "March 1-31, 2026" --due-date 2026-03-15
    python3 generate_invoice.py --invoice-number INV-002 --date 2026-04-01 --period "April 1-30, 2026" --due-date 2026-04-15 --amount 2500
"""
import argparse
from pathlib import Path


def generate_invoice(invoice_number, date, amount, quantity, period, due_date):
    total = amount * quantity
    amount_fmt = f"${amount:,.2f}"
    total_fmt = f"${total:,.2f}"
    qty_fmt = str(int(quantity)) if quantity == int(quantity) else str(quantity)

    html = f"""<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Factura / Invoice {invoice_number}</title>
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
        <!-- Header -->
        <div class="header">
            <div class="company-info">
                <div class="company-name">YOUR NAME HERE</div>
                <div class="company-details">
                    Servicios Digitales y Consultoría<br>
                    Digital Services &amp; Consulting<br>
                    123 Main Street, Suite A<br>
                    City, State 12345<br>
                    Ph. (555) 000-0000<br>
                    RFC: XXXXXXXXXXX
                </div>
            </div>
            <div class="invoice-title">
                <h1>Factura / Invoice</h1>
                <div class="invoice-meta">
                    <div class="meta-box">
                        <div class="meta-label">Fecha / Date</div>
                        <div class="meta-value">{date}</div>
                    </div>
                    <div class="meta-box">
                        <div class="meta-label">Factura #</div>
                        <div class="meta-value">{invoice_number}</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Bill To Section -->
        <div class="bill-to-section">
            <div class="bill-to-header">Facturar a / Bill To</div>
            <div class="bill-to-content">
                Client Corp S.A. de C.V.<br>
                456 Business Avenue, Suite B1<br>
                Colonia Centro<br>
                City, State, Country 00000<br>
                RFC: XXXXXXXXXXX
            </div>
        </div>

        <!-- Terms Section -->
        <div class="terms-section">
            <div class="terms-box">
                <div class="terms-label">Términos / Terms</div>
                <div class="terms-value">Net 15</div>
                <div class="due-date-label">Fecha Límite / Due Date</div>
                <div class="due-date-value">{due_date}</div>
            </div>
        </div>

        <!-- Items Table -->
        <table class="items-table">
            <thead>
                <tr>
                    <th>Fecha / Date</th>
                    <th>Descripción / Description</th>
                    <th>Cantidad / Qty</th>
                    <th>Tarifa / Rate</th>
                    <th>Monto / Amount</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="number-cell">{date}</td>
                    <td class="description-cell">
                        <strong>Servicios Digitales e Inteligencia Estratégica | {period}</strong><br>
                        <strong>Digital Services and Strategic Intelligence | {period}</strong><br><br>

                        Retainer mensual por servicios digitales e inteligencia estratégica incluyendo:<br>
                        Monthly retainer for digital services and strategic intelligence including:<br><br>

                        &bull; Contenido para LinkedIn y sitio web / LinkedIn and web content<br>
                        &bull; Monitoreo de mercado e inteligencia / Market monitoring and intelligence<br>
                        &bull; Mantenimiento de base de datos / Database maintenance<br>
                        &bull; Contenido para inversionistas / Investor-focused content<br>
                        &bull; Reuniones estratégicas y coordinación / Strategic meetings and coordination<br><br>

                        <em>Periodo de servicio / Service Period: {period}</em><br>
                        <em>Referencia / Contract Reference: Service Agreement</em>
                    </td>
                    <td class="number-cell">{qty_fmt}</td>
                    <td class="amount-cell">{amount_fmt}</td>
                    <td class="amount-cell">{total_fmt}</td>
                </tr>
                <tr>
                    <td colspan="5" style="height: 80px; border-left: none; border-right: none; border-bottom: none;"></td>
                </tr>
            </tbody>
        </table>

        <!-- Totals Section -->
        <div class="totals-section">
            <div class="payment-info">
                <strong>Datos Bancarios / Wire Transfer Details:</strong>
                <div class="banking-details">
                    Banco / Bank: Example Bank<br>
                    Cuenta / Account: Your Name<br>
                    No. de Cuenta / Account #: XXXX-XXXX-XXXX<br>
                    Routing #: XXXXXXXXX<br>
                    Swift: XXXXXXXXX<br><br>
                    Correo / Email: you@example.com
                </div>
            </div>
            <table class="totals-table">
                <tr>
                    <td class="totals-label">Subtotal / Subtotal</td>
                    <td class="totals-amount">{total_fmt}</td>
                </tr>
                <tr>
                    <td class="totals-label">Saldo / Amount Due (USD)</td>
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
    parser = argparse.ArgumentParser(description="Generate bilingual HTML invoice")
    parser.add_argument("--invoice-number", required=True, help="e.g. INV-001")
    parser.add_argument("--date", required=True, help="Invoice date, e.g. 3/1/2026")
    parser.add_argument("--amount", type=float, default=1500.00, help="Rate per unit (default: 1500)")
    parser.add_argument("--quantity", type=float, default=1, help="Quantity (default: 1)")
    parser.add_argument("--period", required=True, help='e.g. "March 1-31, 2026"')
    parser.add_argument("--due-date", required=True, help="e.g. 3/15/2026")
    args = parser.parse_args()

    generate_invoice(
        invoice_number=args.invoice_number,
        date=args.date,
        amount=args.amount,
        quantity=args.quantity,
        period=args.period,
        due_date=args.due_date,
    )


if __name__ == "__main__":
    main()
