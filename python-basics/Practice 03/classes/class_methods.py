class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def name(cls):
        print("Class is:", cls.__name__)


print(Math.add(5, 3))
Math.name()