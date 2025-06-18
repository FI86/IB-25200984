# Exemple de classe et methode abstraites

# Imports
# Ancienne methode (Python < 3.4)
# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod

# Classe Animal
# Ancienne methode (Python < 3.4)
# class Animal(metaclass=ABCMeta):
class Animal(ABC):
    """Classe abstraite Animal"""
    @property
    def alimentation(self):
        """Alimentation"""
        return self._aliment

    @alimentation.setter
    def alimentation(self, aliment):
        if aliment in self.regime:
            self._aliment = aliment
        else:
            print(f"Cet animal ne mange pas de {aliment}.")
            self._aliment = None

    @property
    @abstractmethod
    def regime(self):
        pass

    @abstractmethod
    def nourrir(self, heure):
        pass


# Classe Lion
class Lion(Animal):
    """Classe Lion"""
    @property
    def regime(self):
        return ["cheval", "gazelle", "buffle"]

    def nourrir(self, heure):
        if self._aliment:
            print(f"Le lion mange de la viande de {self._aliment} à {heure}")

# Classe Serpent
class Serpent(Animal):
    """Classe Serpent"""
    @property
    def regime(self):
        return ["grenouille", "lapin"]

    def nourrir(self, heure):
        if self._aliment:
            print(f"Le serpent mange de la viande de {self._aliment} à {heure}")

# Programme principal
def main():
    lion = Lion()
    lion.alimentation = "buffle"
    lion.nourrir("12h00")

    serpent = Serpent()
    serpent.alimentation = "grenouille"
    serpent.nourrir("10h00")

    lion.alimentation = "carotte"
    lion.nourrir("15h00")

if __name__ == "__main__":
    main()
