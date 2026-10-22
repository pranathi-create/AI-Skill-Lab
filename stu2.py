"""Collect marks for five students and print their grades."""


def calculate_grade(mark: float) -> str:
    # Boundaries: A = 90-100, B = 80-89.99, C = 70-79.99,
    # D = 60-69.99, and F = 0-59.99.
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "F"


def read_mark(student_name: str) -> float:
    # Keep asking until the user enters a numeric mark in the valid range.
    while True:
        mark_text = input(f"Enter {student_name}'s mark (0-100): ")
        try:
            mark = float(mark_text)
        except ValueError:
            print("Invalid input: enter a number.")
            continue

        if not 0 <= mark <= 100:
            print("Invalid mark: enter a value from 0 to 100.")
            continue

        return mark


def main() -> None:
    students: list[tuple[str, float, str]] = []

    for student_number in range(1, 6):
        name = input(f"Enter the name of student {student_number}: ").strip()
        while not name:
            print("Name cannot be empty.")
            name = input(f"Enter the name of student {student_number}: ").strip()

        mark = read_mark(name)
        students.append((name, mark, calculate_grade(mark)))

    # Print the collected results in aligned columns.
    print("\nSTUDENT MARKS REPORT")
    print("-" * 42)
    print(f"{'Student':<24}{'Mark':>8}  {'Grade':<5}")
    print("-" * 42)
    for name, mark, grade in students:
        print(f"{name:<24}{mark:>8.2f}  {grade:<5}")
    print("-" * 42)


if __name__ == "__main__":
    main()