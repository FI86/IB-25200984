# Exemple de polymorphisme

# Definition de classes
class Animal:
	def crier(self):
		print("un cri d’animal")


class Chien(Animal):
	def crier(self):
		print("whouaf whouaf !")
	
	def crier_comme_un_animal(self):
		super().crier()


class Chat(Animal):
    def crier(self):
        print("miaou !")


# Polymorphisme
animal = Animal()
animal.crier()
animal = Chien()
animal.crier()
animal.crier_comme_un_animal()
animal = Chat()
animal.crier()
