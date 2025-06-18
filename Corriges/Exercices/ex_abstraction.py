# Exercice classe et methode abstraite
# 
# On va utiliser une classe abstraite MoyenPaiement avec une methode abstraite payer(montant) 
# et une methode concrete verifier_connexion() qui affiche "connexion etablie".
# On souhaite avoir 3 moyens de paiement possible : Carte Bancaire, PayPal, ou Cryptomonnaie.
# Chaque moyen de paiement doit pouvoir effectuer un paiement d’un montant donne via la methode payer().

# Imports
from abc import ABC, abstractmethod

# Classe abstraite représentant un moyen de paiement
class MoyenPaiement(ABC):
    """Moyen de paiement"""

    @abstractmethod
    def payer(self, montant):
        """Effectuer un paiement d'un montant donné"""
        pass

    def verifier_connexion(self):
        """Méthode concrète pour simuler la vérification de connexion"""
        print("Connexion au service de paiement établie.")


# Classe concrète : Paiement par Carte Bancaire
class CarteBancaire(MoyenPaiement):
    def payer(self, montant):
        print(f"Paiement de {montant:.2f} € par carte bancaire effectué.")


# Classe concrète : Paiement par PayPal
class PayPal(MoyenPaiement):
    def payer(self, montant):
        print(f"Paiement de {montant:.2f} € via PayPal effectué.")


# Classe concrète : Paiement par Cryptomonnaie
class CryptoMonnaie(MoyenPaiement):
    def payer(self, montant):
        print(f"Paiement de {montant:.2f} € en cryptomonnaie effectué.")


# Traitement d'un paiement
def traitement_paiement(moyen: MoyenPaiement, montant: float):
    moyen.verifier_connexion()
    moyen.payer(montant)

# Programme principal
def main():
    paiements = [CarteBancaire(), PayPal(), CryptoMonnaie()]

    for moyen in paiements:
        traitement_paiement(moyen, 49.99)

if __name__ == "__main__":
    main()
