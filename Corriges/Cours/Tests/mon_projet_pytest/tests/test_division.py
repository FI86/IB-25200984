# Imports
import pytest

from src.calculatrice import division


def test_division_valide():
    assert division(10, 2) == 5

# Test d'erreur de division
def test_division_par_zero():
    with pytest.raises(ValueError, match="Division par zéro"):
        division(10, 0)
        