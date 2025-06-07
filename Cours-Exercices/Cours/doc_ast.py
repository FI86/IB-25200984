# On importe le module 'ast' qui permet d'analyser le code Python sous forme d'arbre syntaxique

# Import path du module os

# On définit le chemin du fichier à analyser : ici, le fichier 'classes.py' situé dans le même dossier que ce script

def extraire_docstrings(fichier):
    pass
    # On ouvre le fichier en lecture avec l'encodage UTF-8

        # On lit le contenu et on le convertit en arbre syntaxique (AST)

    # On parcourt récursivement tous les nœuds de l'arbre (fonctions, classes, modules, etc.)

        # On s'intéresse uniquement aux fonctions, classes et au module lui-même
            # On récupère le nom du nœud (fonction ou classe), ou "Module" si c'est le module principal
            
            # On extrait la docstring associée (si elle existe)
            
            # Si une docstring est trouvée, on l'affiche avec le type de nœud et son nom
            
# Exemple d'utilisation : on appelle la fonction avec le fichier défini plus haut
