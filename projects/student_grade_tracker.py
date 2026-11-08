"""Enter student marks and calculate an average and letter grade."""


def letter_grade(score: float) -> str:
    if not 0 <= score <= 100:
        raise ValueError("Marks must be between 0 and 100.")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def main() -> None:
    name = input("Student name: ").strip()
    if not name:
        print("A student name is required.")
        return

    scores = []
    for subject in ("English", "Mathematics", "Computer Science"):
        try:
            score = float(input(f"{subject} marks (0-100): "))
            letter_grade(score)
        except ValueError as error:
            print(f"Invalid marks: {error}")
            return
        scores.append(score)

    average = sum(scores) / len(scores)
    print(f"Student: {name}")
    print(f"Average: {average:.2f}/100")
    print(f"Grade: {letter_grade(average)}")


if __name__ == "__main__":
    main()
