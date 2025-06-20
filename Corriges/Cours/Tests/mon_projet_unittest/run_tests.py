# Imports
import unittest
from tests.suite_tests import suite

# Programme principal
if __name__ == '__main__':
    # runner permet d'executer une suite de tests.
    # verbosity indique le niveau de detail dans la sortie du test.
    # 2 est le maximum
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
