x = lambda a: a + 10
print(x(5))


multiply = lambda a, b: a * b
print(multiply(5, 6))


sum_three = lambda a, b, c: a + b + c
print(sum_three(5, 6, 2))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))