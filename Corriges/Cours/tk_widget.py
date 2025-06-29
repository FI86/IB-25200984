# Fichier d'exemples de widgets Tkinter
from tkinter import StringVar, Tk, ttk, CENTER, END, DISABLED

root = Tk()

# Label.py
label = ttk.Label(root, text = "Hello, Tkinter!")
label.pack()
label.config(text = "Bonjour")
# wraplength : taille max en pixel avant de passer à la ligne suivante
label.config(wraplength = 200)
label.config(justify = CENTER)
label.config(foreground= 'blue', background= 'yellow')
label.config(font = ("Courier", 18, "bold"))

# Button.py
button = ttk.Button(root, text="Click moi")
button.pack()

def click():
    print("click !")

button.config(command = click)

# Simuler un click sur le bouton
button.invoke()
button.state(["disabled"])
button.invoke()
print(button.instate(["disabled"]))
# pour rendre actif un widget on peut mettre ce qu'on veut sauf "disabled"
# avec la syntaxe button.config(state="...")
# ne fonctionne pas avec button.state()
button.state(["!disabled"])
print(button.instate(["disabled"]))

# Entry.py
entry = ttk.Entry(root, width = 30)
entry.pack()
entry.insert(0, "-Entre ton mot de passe")
entry.delete(0, 1)
entry.config(show = "*")
entry.config(state = DISABLED)
# Ou
entry.state([DISABLED])
entry.state(["disabled"])

entry.state(["!disabled"])
maVariable = entry.get()
print(maVariable)

# Enlève les *
entry.config(show = "")
entry.state(["readonly"])
entry.state(["!readonly"])
entry.delete(0, END)

# StringVar()
monTexte = StringVar()
texte = "Mon texte"
monTexte.set(f"J'ajoute {texte}")
ttk.Entry(root, width = 30, textvariable = monTexte).pack()
monTexte.set("Mon nouveau texte")

def clavier(event):
    touche = event.keysym
    if touche == "Escape": quit()
    if touche == "F1": click()

# Gestion d'événements
root.bind("<Key>", clavier)

root.mainloop()
