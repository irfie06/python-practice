"""Simple in-memory expense tracker using Python lists and dictionaries."""


def main() -> None:
    expenses = []
    print("Expense Tracker (type 'done' to finish)")
    while True:
        category = input("Category: ").strip()
        if category.lower() == "done":
            break
        if not category:
            print("Enter a category.")
            continue
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
        except ValueError as error:
            print(f"Invalid amount: {error}")
            continue
        expenses.append({"category": category, "amount": amount})

    if not expenses:
        print("No expenses recorded.")
        return

    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]

    print("\nSpending by category:")
    for category, amount in sorted(totals.items()):
        print(f"{category}: {amount:.2f}")
    print(f"Total spent: {sum(totals.values()):.2f}")


if __name__ == "__main__":
    main()
