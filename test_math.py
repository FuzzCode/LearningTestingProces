import unittest
from my_math import add  # Załóżmy, że funkcja add jest w pliku my_math.py
from my_math import find_max  # Importujemy funkcję do testowania

class TestsFunction(unittest.TestCase):
    def test_find_max_with_positive_numbers(self):
        self.assertEqual(find_max([1, 2, 3, 4, 5]), 5)

    def test_find_max_with_negative_numbers(self):
        self.assertEqual(find_max([-10, -5, -2, -1]), -1)

    def test_find_max_with_mixed_numbers(self):
        self.assertEqual(find_max([-10, 0, 10, 5]), 10)

    def test_find_max_with_single_element(self):
        self.assertEqual(find_max([42]), 42)

    def test_find_max_with_empty_list(self):
        self.assertIsNone(find_max([]))  # Sprawdzamy, czy zwraca None dla pustej listy

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-2, 3), 1)

if __name__ == "__main__":
    unittest.main()
