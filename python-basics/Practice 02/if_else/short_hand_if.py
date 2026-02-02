a = 5
b = 2
if a > b: print("a is greater")

a = 10
b = 20
bigger = a if a > b else b   # үлкенін таңдайды
print(bigger)

username = ""
name = username if username else "Guest"
print(name)