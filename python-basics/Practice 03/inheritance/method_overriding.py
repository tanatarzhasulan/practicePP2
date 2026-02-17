class Animal:
    def speak(self):
        print("Some sound")


class Dog(Animal):
    def speak(self):
        print("Woof!")


a = Animal()
d = Dog()

a.speak()
d.speak()