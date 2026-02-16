# numbers = list(map(int, input().split()))
# print(len(numbers))
a, b, k = map(int, input().split())
count = 0
for i in range(a,b+1):
    if i%k==0:
        count += 1
print(count)