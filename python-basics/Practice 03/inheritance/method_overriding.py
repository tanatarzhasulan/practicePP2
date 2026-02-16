n = int(input())
numbers = list(map(int, input().split()))

numbers.sort()
numbers.reverse()
print(*numbers)