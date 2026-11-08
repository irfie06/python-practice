"""A simple command-line calculator for basic arithmetic."""


def calculate(first: float, operator: str, second: float) -> float:
    """Calculate a result for one of four supported operators."""
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first / second
    raise ValueError("Choose one of: +, -, *, /.")


def main() -> None:
    print("Simple Calculator")
    try:
        first = float(input("First number: "))
        operator = input("Operator (+, -, *, /): ").strip()
        second = float(input("Second number: "))
        result = calculate(first, operator, second)
    except (ValueError, ZeroDivisionError) as error:
        print(f"Error: {error}")
    else:
        print(f"Result: {result:g}")


if __name__ == "__main__":
    main()
