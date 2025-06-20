# Imports
import pytest

from src.calculatrice import addition

# Test de base
def test_addition_simple():
    assert addition(2, 3) == 5

def test_addition_negative():
    assert addition(-1, -1) == -2


# Test avec plusieurs valeurs
@pytest.mark.parametrize("a, b, result", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])

def test_addition(a, b, result):
    assert addition(a, b) == result

# Test avec des données réutilisable
@pytest.fixture
def donnees():
    return {"a": 10, "b": 5}

def test_soustraction(donnees):
    assert donnees["a"] - donnees["b"] == 5

    