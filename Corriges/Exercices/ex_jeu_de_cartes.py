# Exercice jeu de cartes
# 
# Définissez une classe JeuDeCartes() permettant d’instancier des objets dont
# le comportement soit similaire à celui d’un vrai jeu de cartes. 
# La classe devra comporter au moins les quatre méthodes suivantes :

# Méthode constructeur : Création et remplissage d’une liste de 52 éléments. 
# Ces éléments sont des tuples contenant la couleur (Coeur, Trèfle, Pique, Carreau)
# et la valeur (2, 3, 4, 5, 6, 7, 8, 9, 10, Valet, Dame, Roi, As) de chacune des cartes.
# Dans une telle liste, l’élément (Valet , Pique) désigne donc le Valet de Pique, et la 
# liste terminée doit être sous la forme : [(2, Coeur), (3, Coeur), ....., (As, Carreau)].

# Méthode nom_carte() : cette méthode doit renvoyer, sous la forme d’une chaîne,
# l’identité d’une carte quelconque dont on lui a fourni le tuple descripteur en argument.
# Par exemple, l’instruction : 
# print(jeu.nom_carte((valeur, couleur))) doit provoquer l’affichage de : 2 de Carreau

# Méthode melanger() : Cette méthode sert à mélanger les éléments de la liste
# contenant les cartes, quel qu’en soit le nombre. 

# Méthode tirer() : lorsque cette méthode est invoquée,
# la première carte de la liste est retirée du jeu.
# Le tuple contenant sa valeur et sa couleur est renvoyé au programme appelant. 
# Si cette méthode est invoquée alors qu’il ne reste plus aucune carte dans la liste,
# il faut alors renvoyer None au programme appelant.

from random import shuffle

class JeuDeCartes:
    """Classe Jeu de Cartes"""

    def __init__(self):
        self.couleurs = ("Coeur", "Carreau", "Trefle", "Pique")
        self.valeurs = (2, 3, 4, 5, 6, 7, 8, 9, 10, "Valet", "Dame", "Roi", "As")
        self.cartes = []
        
        for couleur in self.couleurs:
            for valeur in self.valeurs:
                self.cartes.append((valeur, couleur))
        
    def nom_carte(self, carte):
        return f"{carte[0]} de {carte[1]}"

    def melanger(self):
        shuffle(self.cartes)

    def tirer(self):
        if len(self.cartes) != 0: return self.cartes.pop(0)
        else: return None

def main():
    jeu = JeuDeCartes()
    jeu.melanger()
    index = 0
    
    while (len(jeu.cartes) != 0):
        index += 1
        c = jeu.tirer()
        print(f"{index:02d} - {jeu.nom_carte(c)}")

    input("Appuyer sur une <Entrée> pour terminer !")

if __name__ == "__main__":
    main()
