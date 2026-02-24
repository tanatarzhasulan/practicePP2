'''
def square_generator(n):
    for i in range(n + 1):
        yield i*i

n = 5
for value in square_generator(n):
    print(value) 
'''


'''
def even_numbers(n):
    for i in range(n+1):
        if i%2==0:
            yield i

n = int(input())

result = ",".join(str(num) for num in even_numbers(n))
print(result)
'''

def divisible3_4(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i

a = 48
for el in divisible3_4(a):
    print(el)



def squares(a, b):
    for i in range(a, b+1):
        yield i*i

c, d = 3, 8
for el in squares(c, d):
    print(el)



def decreasing(k):
    for i in range(k, -1, -1):
        yield i

b = 7
res = decreasing(b)
for num in res:
    print(num)
