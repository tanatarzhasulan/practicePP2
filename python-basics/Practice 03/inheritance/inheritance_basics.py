n = int(input())
numbers = list(map(int, input().split()))

num_min = min(numbers)
num_max = max(numbers)

for i in range(n):
    if numbers[i]==num_max:
        numbers[i]=num_min

print(*numbers)
