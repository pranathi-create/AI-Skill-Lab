"""Collect marks for five students and display their letter grades."""


def grade_for(mark: float) -> str:
    """Return the letter grade for a mark from 0 through 100."""
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "F"


def main() -> None:
    students: list[tuple[str, float, str]] = []

    for number in range(1, 6):
        name = input(f"Enter the name of student {number}: ").strip()
        while not name:
            print("Name cannot be empty.")
            name = input(f"Enter the name of student {number}: ").strip()

        while True:
            mark_text = input(f"Enter {name}'s mark (0-100): ")
            try:
                mark = float(mark_text)
            except ValueError:
                print("Invalid input. Enter a numeric mark from 0 to 100.")
                continue

            if not 0 <= mark <= 100:
                print("Mark out of range. Enter a mark from 0 to 100.")
                continue

            students.append((name, mark, grade_for(mark)))
            break

    print("\nStudent Results")
    print("-" * 42)
    print(f"{'Name':<24}{'Mark':>8}  {'Grade':<5}")
    print("-" * 42)
    for name, mark, grade in students:
        print(f"{name:<24}{mark:>8.2f}  {grade:<5}")
    print("-" * 42)


if __name__ == "__main__":
    main()