# Imports
import unittest
from tests.test_addition import TestAddition
from tests.test_multiplication import TestMultiplication
from tests.test_division import TestDivision

def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestAddition))
    suite.addTest(loader.loadTestsFromTestCase(TestMultiplication))
    suite.addTest(loader.loadTestsFromTestCase(TestDivision))
    return suite
    
    # Ancienne facon de faire avant python 3.11
    # et supprimer avec la version 3.13
    # suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(TestAddition))
    # suite.addTest(unittest.makeSuite(TestMultiplication))
    # suite.addTest(unittest.makeSuite(TestDivision))
    # return suite
