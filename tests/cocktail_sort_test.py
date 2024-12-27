import unittest
from codefiles.cocktail_sort import cocktailSort

class TestcocktailSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(cocktailSort([]), [])

    def test_single_element(self):
        self.assertEqual(cocktailSort([1]), [1])

    def test_sorted_list(self):
        self.assertEqual(cocktailSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(cocktailSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(cocktailSort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_list_with_duplicates(self):
        self.assertEqual(cocktailSort([4, 4, 4, 4]), [4, 4, 4, 4])

    def test_negative_numbers(self):
        self.assertEqual(cocktailSort([-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]), [-9, -6, -5, -5, -5, -4, -3, -3, -2, -1, -1])

    def test_mixed_numbers(self):
        self.assertEqual(cocktailSort([3, -1, 4, 1, -5, 9, -2, 6, -5, 3, 5]), [-5, -5, -2, -1, 1, 3, 3, 4, 5, 6, 9])

if __name__ == '__main__':
    unittest.main()
