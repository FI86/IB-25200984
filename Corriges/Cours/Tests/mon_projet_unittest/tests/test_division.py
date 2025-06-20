# Imports
import unittest
from src.calculatrice import division

# Classe de test division
class TestDivision(unittest.TestCase):
    # Avant chaque test
    def setUp(self):
        print("Préparation des données de division")
        self.a = 10
        self.b = 2

    # Apres chaque test
    def tearDown(self):
        print("Nettoyage après un test de division")
        del self.a
        del self.b
    
    def test_division_valide(self):
        self.assertAlmostEqual(division(10, 2), 5.0)

    def test_division_negative(self):
        self.assertAlmostEqual(division(-9, 3), -3.0)

    def test_division_par_zero(self):
        with self.assertRaises(ValueError):
            division(10, 0)
