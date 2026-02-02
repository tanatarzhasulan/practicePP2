# and, or, not

x = True
y = False

print(x and y)   # False
print(x or y)    # True
print(not x)     # False


def myFunction():
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")

# isinstance() example
n = 200
print(isinstance(n, int))  # True