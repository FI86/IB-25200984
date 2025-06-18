# Exercice propriete, encapsulation et destructeur
# Créez une classe Animal :
#     Attributs privés : _nom, _age
#     Propriétés pour accéder et modifier nom et age avec vérification (âge >= 0).
#     Une méthode parler() qui affiche "L'animal fait un bruit."
#     Un destructeur qui affiche : "{nom} a été retiré du zoo."
# Créez deux classes filles :
#     Chien, redéfinit parler() → affiche "{nom} aboie : Woof!"
#     Chat,  redéfinit parler() → affiche "{nom} miaule : Miaou!"
# Créez une fonction faire_parler(animal) qui prend un objet Animal et appelle sa méthode parler().


# Classe Animal
class Animal:
    # Constructeur
    def __init__(self, nom, age):
        self._nom = nom
        self._age = age

    # Proprietes
    @property
    def nom(self):
        return self._nom

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("L'âge ne peut pas être négatif.")
        self._age = value

    # Methode parler
    def parler(self):
        print("L'animal fait un bruit.")

    # Destructeur
    def __del__(self):
        print(f"{self.nom} a été retiré du zoo.")


# Classe Chien
class Chien(Animal):
    def parler(self):
        print(f"{self.nom} aboie : Woof!")


# Classe Chat
class Chat(Animal):
    def parler(self):
        print(f"{self.nom} miaule : Miaou!")


# Fonction qui fait parler un animal
def faire_parler(animal :Animal):
        animal.parler()


# Programme principal
if __name__ == "__main__":
    animal = Animal("toto", 4)
    rex = Chien("Rex", 5)
    minou = Chat("Minou", 3)
    faire_parler(animal)
    faire_parler(rex)
    faire_parler(minou)

    # La fin de programme déclenche le destrcuteur __del__ pour chaque objet crée.