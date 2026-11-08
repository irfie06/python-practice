"""Summarize a sample shop's sales using only Python's standard library.

Usage:
    python3 sales_analyzer.py
    python3 sales_analyzer.py data/sample_sales.csv
"""

import csv
import sys
from collections import defaultdict
from pathlib import Path


def analyze_sales(csv_path: Path) -> dict:
    """Read a CSV file and calculate sales by product and category."""
    product_totals = defaultdict(float)
    category_totals = defaultdict(float)
    order_count = 0
    total_revenue = 0.0

    with csv_path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        required = {"date", "product", "category", "quantity", "unit_price"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError(f"CSV must contain: {', '.join(sorted(required))}")

        for line_number, row in enumerate(reader, start=2):
            try:
                quantity = int(row["quantity"])
                price = float(row["unit_price"])
                if quantity < 0 or price < 0:
                    raise ValueError("quantity and price cannot be negative")
                if not row["product"] or not row["category"]:
                    raise ValueError("product and category cannot be empty")
            except (ValueError, TypeError) as error:
                raise ValueError(f"Invalid data on CSV line {line_number}: {error}") from error

            revenue = quantity * price
            total_revenue += revenue
            product_totals[row["product"]] += revenue
            category_totals[row["category"]] += revenue
            order_count += 1

    return {
        "orders": order_count,
        "total_revenue": total_revenue,
        "product_totals": dict(product_totals),
        "category_totals": dict(category_totals),
    }


def display_report(report: dict) -> None:
    print("SALES ANALYSIS REPORT")
    print("=" * 32)
    print(f"Sales records: {report['orders']}")
    print(f"Total revenue: PKR {report['total_revenue']:,.2f}")

    print("\nRevenue by category:")
    for category, amount in sorted(
        report["category_totals"].items(), key=lambda item: -item[1]
    ):
        print(f"  {category:<18} PKR {amount:,.2f}")

    print("\nRevenue by product:")
    for product, amount in sorted(
        report["product_totals"].items(), key=lambda item: -item[1]
    ):
        print(f"  {product:<18} PKR {amount:,.2f}")


def main() -> None:
    default_path = Path(__file__).resolve().parent / "data" / "sample_sales.csv"
    csv_path = Path(sys.argv[1]) if len(sys.argv) > 1 else default_path

    try:
        report = analyze_sales(csv_path)
        display_report(report)
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
