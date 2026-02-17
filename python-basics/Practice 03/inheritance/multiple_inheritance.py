class Fly:
    def move(self):
        print("Flying")


class Swim:
    def move(self):
        print("Swimming")


class Duck(Fly, Swim):
    pass


d = Duck()
d.move()