# '''class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(self.name, self.age)

# s1 = Student("Emil", 18)
# s2 = Student("Tobias", 20)

# s1.info()
# s2.info() '''

# n = int(input())








class S_numbers:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.n:
            self.current += 1
            return self.current ** 2
        else:
            raise StopIteration

k = int(input())
counter = S_numbers(k)        
for el in counter:
    print(el) 
