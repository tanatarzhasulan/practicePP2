n = int(input())

isPrime = False
for i in range(2, n//2+1):
    if n%2==0:
        isPrime = True
        break
if isPrime:
    print('No')
else:
    print('Yes')