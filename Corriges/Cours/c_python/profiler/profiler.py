import cProfile
import time

def function_a():
    """Fonction qui simule un travail long."""
    time.sleep(0.2)  # Simule un délai de 200ms
    print("Fonction A terminée")

def function_b():
    """Fonction qui simule un travail moyen."""
    time.sleep(0.5)  # Simule un délai de 500ms
    print("Fonction B terminée")

def function_c():
    """Fonction qui fait un travail rapide."""
    time.sleep(0.1)  # Simule un délai de 100ms
    print("Fonction C terminée")

def main():
    """Fonction principale qui appelle toutes les autres."""
    function_a()
    function_b()
    function_c()

# Profiler le programme entier
cProfile.run('main()')
