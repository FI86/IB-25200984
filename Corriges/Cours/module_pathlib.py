# Fichier d'exemples avec le module pathlib

# Imports
from pathlib import Path
import datetime
import time
import platform

def main():
    chemin = Path(__file__).parent
    nom_fichier = chemin / "osFichierTest.txt"

    # Afficher le chemin courant, le nom de l'OS
    print(chemin)
    print(Path(nom_fichier).name)
    print(Path.cwd())
    print(platform.system())

    # Vérification de l'existence d'un élément et de son type
    print(f"L'élément existe : {nom_fichier.exists()}")
    print(f"L'élément est un fichier : {nom_fichier.is_file()}")
    print(f"L'élément est un dossier : {nom_fichier.is_dir()}")

    # Manipuler les informations sur le chemin du fichier
    print(f"Le chemin du fichier : {nom_fichier.resolve()}")
    print(f"Le chemin du fichier et sa désignation : {nom_fichier.resolve().parent, nom_fichier.name}")

    # Obtenir la date de modification du fichier
    print(f"Date de modification du fichier : {time.ctime(nom_fichier.stat().st_mtime)}")
    print(f"Date de modification du fichier : {datetime.datetime.fromtimestamp(nom_fichier.stat().st_mtime)}")
    # Calculer le temps écoulé depuis la dernière modification
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(nom_fichier.stat().st_mtime)
    print(f"Il s'est passé {td} depuis la dernière modification")
    print(f"Ou, {td.total_seconds()} secondes")
    


if __name__ == "__main__":
    main()
