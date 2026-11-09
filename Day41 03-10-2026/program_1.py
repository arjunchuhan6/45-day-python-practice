"""Basic unit testing example.

Steps:
1. Write the function that needs to be tested.
2. Create a test class using unittest.TestCase.
3. Call the function inside a test method.
4. Use assertEqual() to compare the actual and expected results.
5. Run this file with: python program_1.py
"""

import unittest


def add_numbers(first_number: int, second_number: int) -> int:
    """Return the sum of two numbers."""

    return first_number + second_number


class TestAddNumbers(unittest.TestCase):
    """Unit tests for add_numbers()."""

    def test_add_two_numbers(self) -> None:
        """The function should return the correct sum."""

        result = add_numbers(2, 3)

        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()