# a, b = map(int, input().split())
# res = a**2 + b**2
# print(res)

numbers = list(map(int, input().split()))
t = sum(numbers)/len(numbers)
count = 0
for i in range(len(numbers)):
    if numbers[i]>t:
        count += 1
print(count)