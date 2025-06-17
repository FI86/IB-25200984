# Exercice generateur
# 
# Ecrire un générateur en Python qui génère tous les nombres pairs jusqu'à un nombre donné n. 
# Le générateur doit s'arrêter lorsque le nombre généré est supérieur à n.

# Generateur
def generateur(n):
    num = 0
    while num <= n:
        yield num
        num += 2

# Utilisation du générateur
n = 10
gen = generateur(n)

for elem in gen:
    print(elem)
