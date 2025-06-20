# fichier: main.py
from ctypes import CDLL, c_int
from os import path

CHEMIN = path.dirname(__file__)

lib = CDLL(CHEMIN + '/exemple.dll')
lib.bonjour()

# definition des types d'argument et du type de retour
lib.addition.argtypes = [c_int, c_int]
lib.addition.restype = c_int
print("resultat de l'addition 5 + 3 :", lib.addition(5, 3))
