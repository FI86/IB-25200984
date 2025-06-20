# Imports
import unittest
from src.calculatrice import addition

# Classe de test addition
class TestAddition(unittest.TestCase):
    # Avant chaque test
    def setUp(self):
        print("Préparation des données d’addition")
        self.a = 4
        self.b = 5

    # Apres chaque test
    def tearDown(self):
        print("Nettoyage après un test d’addition")
        del self.a
        del self.b

    def test_addition_positive(self):
        self.assertEqual(addition(4, 5), 9)

    def test_addition_negative(self):
        self.assertEqual(addition(-3, -7), -10)

    def test_addition_mixed(self):
        self.assertEqual(addition(-2, 5), 3)
