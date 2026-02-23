mytuple = ("apple", "banana", "cherry")
myittuple = iter(mytuple)

print(next(myittuple))
print(next(myittuple))
print(next(myittuple))

mystr = "banana"
myitstr = iter(mystr)

print(next(myitstr))
print(next(myitstr))
print(next(myitstr))
print(next(myitstr))
print(next(myitstr))
print(next(myitstr))

for x in mytuple:
    print(x)

for x in mystr:
    print(x)