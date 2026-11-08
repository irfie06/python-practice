"""A command-line calculator with safe input handling."""


def calculate(first: float, second: float, operator: str) -> float:
    """Return the result of a basic arithmetic operation."""
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
    raise ValueError("Choose +, -, * or /.")


def main() -> None:
    print("Simple Calculator")
    try:
        first = float(input("First number: "))
        operator = input("Operation (+, -, *, /): ").strip()
        second = float(input("Second number: "))
        print(f"Result: {calculate(first, second, operator):g}")
    except (ValueError, ZeroDivisionError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
