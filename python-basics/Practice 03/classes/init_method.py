class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


s1 = Student("Emil", 18)
s2 = Student("Tobias", 20)

s1.info()
s2.info()