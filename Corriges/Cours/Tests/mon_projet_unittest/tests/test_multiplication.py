# Imports
import unittest
from src.calculatrice import multiplication

# Classe de test division
class TestMultiplication(unittest.TestCase):
    def test_multiplication_positive(self):
        self.assertEqual(multiplication(3, 4), 12)

    def test_multiplication_negative(self):
        self.assertEqual(multiplication(-2, 5), -10)

    def test_multiplication_zero(self):
        self.assertEqual(multiplication(0, 10), 0)
