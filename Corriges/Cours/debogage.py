# Imports
import pdb
import sys

# Fonction division pouvant provoquer une erreur
def division(a, b):
    return a / b

# Fonction principale
def main():
    try:
        # provocation de l'erreur de division par 0
        result = division(10, 0)
    except Exception:
        # sys.exc_info() retourne un tuple (type, value, traceback) de la dernière exception attrapée.
        _, _, tb = sys.exc_info()
        # recupere le traceback pour faire l'analyse post mortem
        pdb.post_mortem(tb)

# Appel de la fonction principale
if __name__ == "__main__":
    main()
