"""Tests for sales_analyzer.py. Run: python3 -m unittest discover -s tests"""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from sales_analyzer import analyze_sales


class SalesAnalyzerTests(unittest.TestCase):
    def test_summary(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_file = Path(temp_dir) / "sales.csv"
            csv_file.write_text(
                "date,product,category,quantity,unit_price\n"
                "2026-10-01,Pen,Stationery,2,50\n"
                "2026-10-02,Pen,Stationery,3,50\n"
                "2026-10-03,Mouse,Accessories,1,500\n",
                encoding="utf-8",
            )
            report = analyze_sales(csv_file)
            self.assertEqual(report["orders"], 3)
            self.assertEqual(report["total_revenue"], 750)
            self.assertEqual(report["product_totals"]["Pen"], 250)
            self.assertEqual(report["category_totals"]["Accessories"], 500)

    def test_invalid_data(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_file = Path(temp_dir) / "sales.csv"
            csv_file.write_text(
                "date,product,category,quantity,unit_price\n"
                "2026-10-01,Pen,Stationery,-2,50\n",
                encoding="utf-8",
            )
            with self.assertRaises(ValueError):
                analyze_sales(csv_file)


if __name__ == "__main__":
    unittest.main()
