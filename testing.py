"""
Performing Unit tests for the Differentiation Engine and files.
Run by using: python '-m' unittest discover tests in the terminal.
"""

import unittest
from algebraic import diffren_algebraic
from trigonometry import diffren_trigonometric
from logarithmic import diffren_logarithmic

class TestDifferentiationEngine(unittest.TestCase):

    def test_algebraic(self):
        self.assertEqual(diffren_algebraic(3, 4, "x"), "12*x^3")
        self.assertEqual(diffren_algebraic(5, 0, "x"), "0")
        self.assertEqual(diffren_algebraic(2, 1, "x"), "2")

    def test_trigonometric(self):
        self.assertEqual(diffren_trigonometric(3, 1, "sin", "x"), "3*cos(x)")
        self.assertEqual(diffren_trigonometric(3, 2, "cosec", "x"), "-6*cosec(x)^2*cot(x)")
        self.assertEqual(diffren_trigonometric(4, 0, "tan", "x"), "0")

    def test_logarithmic(self):
        self.assertEqual(diffren_logarithmic(2, 1, "x"), "2*(1/x)")
        self.assertEqual(diffren_logarithmic(3, 0, "x"), "0")

if __name__ == '__main__':
    unittest.main()