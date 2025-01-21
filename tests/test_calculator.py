import unittest
from string_calculator.calculator import add

class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_single_number(self):
        self.assertEqual(add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(add("1,5"), 6)

    def test_multiple_numbers(self):
        self.assertEqual(add("1,2,3,4"), 10)

    def test_newline_delimiter(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)

    def test_negative_number(self):
        with self.assertRaises(ValueError) as context:
            add("1,-2,3")
        self.assertEqual(str(context.exception), "negative numbers not allowed: -2")

    def test_multiple_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            add("-1,-2,3")
        self.assertEqual(str(context.exception), "negative numbers not allowed: -1, -2")

    def test_ignore_large_numbers(self):
        self.assertEqual(add("2,1001"), 2)

    def test_custom_delimiter_of_any_length(self):
        self.assertEqual(add("//[***]\n1***2***3"), 6)

    def test_multiple_custom_delimiters(self):
        self.assertEqual(add("//[*][%]\n1*2%3"), 6)

    def test_multiple_custom_delimiters_longer_than_one_char(self):
        self.assertEqual(add("//[**][%%]\n1**2%%3"), 6)

if __name__ == "__main__":
    unittest.main()
