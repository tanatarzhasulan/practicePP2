class Dog:
    species = "Canis familiaris"

    def __init__(self, name):
        self.name = name


d1 = Dog("Buddy")
d2 = Dog("Max")

print(Dog.species)
print(d1.name, d1.species)
print(d2.name, d2.species)

Dog.species = "Dog"
print(d1.species, d2.species)