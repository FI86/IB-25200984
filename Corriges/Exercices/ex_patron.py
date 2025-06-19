# Exercice patron de conception

# Un centre météorologique souhaite développer un système de notifications.
# Lorsqu'une mise à jour de la température est enregistrée, 
# plusieurs dispositifs doivent être informés automatiquement :
#     Une application mobile
#     Un panneau d'affichage
#     Un site web
# Implémente le design pattern Observer pour :
#     Créer une classe StationMeteo (le sujet/observable) qui contient la température actuelle.
#     Permettre aux dispositifs (observateurs) d'être ajouté ou retiré.
#     Informer automatiquement tous les observateurs ajoutés à chaque mise à jour de température.
# Contraintes :
#     Chaque observateur doit implémenter une méthode mise_a_jour(temp) qui affiche un message personnalisé.
#     Tu dois utiliser des classes Python pour structurer le tout.

# Imports
from abc import ABC, abstractmethod

# L'observateur générique
class Observateur(ABC):
    @abstractmethod
    def mise_a_jour(self, temperature):
        pass

# Le sujet
class StationMeteo:
    def __init__(self):
        self._observateurs = []
        self._temperature = None

    def ajouter_observateur(self, obs):
        self._observateurs.append(obs)

    def retirer_observateur(self, obs):
        self._observateurs.remove(obs)

    def notifier_observateurs(self):
        for obs in self._observateurs:
            obs.mise_a_jour(self._temperature)

    def nouvelle_temperature(self, temp):
        print(f"[Station] Température mise à jour : {temp} °C")
        self._temperature = temp
        self.notifier_observateurs()


# Observateur 1 : Application mobile
class ApplicationMobile(Observateur):
    def mise_a_jour(self, temperature):
        print(f"[App Mobile] Nouvelle température reçue : {temperature} °C")


# Observateur 2 : Panneau d'affichage
class PanneauAffichage(Observateur):
    def mise_a_jour(self, temperature):
        print(f"[Panneau] Température affichée : {temperature} °C")


# Observateur 3 : Site web
class SiteWeb(Observateur):
    def mise_a_jour(self, temperature):
        print(f"[Site Web] Température en ligne : {temperature} °C")


# Programme principal
def main():
    # Station météo
    station = StationMeteo()
    
    # Dispositifs
    app = ApplicationMobile()
    panneau = PanneauAffichage()
    site = SiteWeb()

    # Ajout des dispositifs dans la station météo
    station.ajouter_observateur(app)
    station.ajouter_observateur(panneau)
    station.ajouter_observateur(site)

    # Affectations d'une temperature
    station.nouvelle_temperature(25)

    # Retrait d'un dispositif
    station.retirer_observateur(panneau)
    # Affectations d'une nouvelle temperature
    station.nouvelle_temperature(30)

# Execution du programme principal
if __name__ == "__main__":
    main()
