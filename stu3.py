"""Check student marks and calculate their average."""

import unittest


def calculate_average(marks: list[int | float]) -> float:
    """Return the mean of marks from 0 through 100.

    Raises ValueError for an empty list or a mark outside the allowed range.
    Raises TypeError if a mark is not a number (booleans are not accepted).
    """
    if not marks:
        raise ValueError("marks must not be empty")

    for mark in marks:
        if isinstance(mark, bool) or not isinstance(mark, (int, float)):
            raise TypeError("each mark must be a number")
        if not 0 <= mark <= 100:
            raise ValueError("each mark must be between 0 and 100")

    # This calculates the mean without changing the original list.
    return sum(marks) / len(marks)


class CalculateAverageTests(unittest.TestCase):
    def test_normal_values(self) -> None:
        self.assertEqual(calculate_average([70, 80, 90]), 80)

    def test_boundary_values(self) -> None:
        self.assertEqual(calculate_average([0, 100]), 50)

    def test_rejects_empty_list(self) -> None:
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_rejects_marks_below_and_above_range(self) -> None:
        for marks in ([-1], [101]):
            with self.subTest(marks=marks):
                with self.assertRaises(ValueError):
                    calculate_average(marks)

    def test_rejects_non_numeric_mark(self) -> None:
        with self.assertRaises(TypeError):
            calculate_average([75, "80"])  # type: ignore[list-item]

    def test_preserves_original_list(self) -> None:
        marks = [65, 75, 85]
        original = marks.copy()

        calculate_average(marks)

        self.assertEqual(marks, original)


def main() -> None:
    marks: list[float] = []
    print("Enter marks from 0 to 100. Press Enter on a blank line when finished.")

    while True:
        mark_text = input("Mark: ").strip()
        if not mark_text:
            break

        try:
            mark = float(mark_text)
        except ValueError:
            print("Invalid: please enter a numeric mark from 0 to 100.")
            continue

        if not 0 <= mark <= 100:
            print("Invalid: the mark must be between 0 and 100.")
            continue

        marks.append(mark)
        print(f"Valid mark: {mark:g}")

    try:
        print(f"Average: {calculate_average(marks):.2f}")
    except ValueError as error:
        print(f"Cannot calculate average: {error}")


if __name__ == "__main__":
    main()