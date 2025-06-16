# Exercice boucles imbriquees
# 
# Ecrivez un programme qui affiche les 20 premiers resultats de la table 
# de multiplication par un nombre entre par l’utilisateur
# Demander à l’utilisateur de rejouer.
# « Voulez-vous rejouer ? » Réponse possible oui ou non

def main():
    reponse = ""

    while reponse.upper() != "NON":
        valeur = input("Quelle table de multiplication : ")

        for x in range(1, 21):
            print(f"{valeur} x {x} = {int(valeur) * x}")
        
        reponse = input("Voulez-vous rejouer ? ")

if __name__ == "__main__":
    main()
    