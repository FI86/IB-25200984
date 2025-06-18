class Vehicule:
    """classe véhicule"""
    def __init__(self):
        self._vitesse = 0
        self.__nbRoues = 4

    @property
    def nbRoues(self):
        print("Lecture propriété nbRoues : ")
        return self.__nbRoues

    @property
    def vitesse(self):
        return self._vitesse

    @vitesse.setter
    def vitesse(self, vitesse):
        self._vitesse = vitesse

    @nbRoues.setter
    def nbRoues(self, nbRoues):
        print(f"Modification propriété nbRoues : {nbRoues}")
        self.__nbRoues = nbRoues

    @nbRoues.deleter
    def nbRoues(self):
        print("Réinitialisation propriété nbRoues : RAZ effectuée")
        self.__nbRoues = 0
        # del self.__nbRoues

    def accelerer(self, delta_vitesse):
        self._vitesse += delta_vitesse

    def decelerer(self, delta_vitesse):
        self._vitesse -= delta_vitesse
    

class Voiture(Vehicule):
    """classe Voiture"""
    def __init__(self, klaxon="tût tût !"):
        super().__init__()
        self.klaxon = klaxon

    def klaxonner(self):
        print(self.klaxon)


def main():
    v = Voiture()
    v.vitesse = 50
    v.accelerer(20)
    v.accelerer(30)
    v.decelerer(10)
    v.klaxonner()

    print(v.vitesse)
    # par convention le _ indique que l'attribut est privé
    # mais cela ne provoque pas d'erreur d'y accéder
    print(v._vitesse) 

    print(v.nbRoues)
    v.nbRoues = 3
    print(v.nbRoues)
    del v.nbRoues
    print(v.nbRoues)

    # print(v.__nbRoues)
    # provoque une erreur

if __name__ == "__main__":
    main()
    