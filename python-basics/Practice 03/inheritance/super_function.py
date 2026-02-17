class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group

    def info(self):
        print(self.name, self.group)


s = Student("Emil", "SE-101")
s.info()