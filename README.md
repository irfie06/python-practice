# Python Practice and Sales Analytics

A beginner-friendly collection of real Python scripts with an applied business data analysis example. Written as educational examples, not as claims of professional production experience.

## Featured project: Sales Analyzer

The [Sales Analyzer](sales_analyzer.py) reads sales records from a CSV file and generates a summary showing:

- Total revenue and the number of sales records
- Revenue by product
- Revenue by category
- Helpful error messages for missing files and invalid data

**Project files**

| File | Description |
| --- | --- |
| [sales_analyzer.py](sales_analyzer.py) | Main Python application |
| [data/sample_sales.csv](data/sample_sales.csv) | Fictional sample shop sales |
| [tests/test_sales_analyzer.py](tests/test_sales_analyzer.py) | Automated unit tests |

### Run on your Mac or another computer

Install Python 3, download or clone this repository, open Terminal in the downloaded folder, and run:

```bash
python3 sales_analyzer.py
```

To analyze a different CSV file using the same column layout:

```bash
python3 sales_analyzer.py data/sample_sales.csv
```

Run tests:

```bash
python3 -m unittest discover -s tests
```

No third-party libraries or API keys are required.

### Input format

The input CSV needs these headers: `date,product,category,quantity,unit_price`. Prices are illustrative Pakistani rupee values. This is fictional practice data, not actual customer or business records.

## Other Python examples

| File | Purpose |
| --- | --- |
| [Calculator](projects/calculator.py) | Basic arithmetic with input validation |
| [Student Grade Tracker](projects/student_grade_tracker.py) | Average marks and grade calculation |
| [Expense Tracker](projects/expense_tracker.py) | Track and summarize expenses within a session |
| [Original Calculator](calculator.py) | Another basic calculator implementation |

## About

This repository supports the learning journey of **Irfan Hussain**, a **Business Data Analytics student at COMSATS University Islamabad**, with a focus on Python fundamentals, databases, and practical data analysis.

## Project status

The scripts and sample dataset are available to explore. The sales data is fictional, and the project is intended for learning and portfolio development.
