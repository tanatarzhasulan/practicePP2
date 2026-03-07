def squares(n):
    for i in range(1, n+1):
        yield i*i

n = int(input())

for i in squares(n):
    print(i)