nlr = list(map(int, input().split()))
n, l, r = nlr[0], nlr[1], nlr[2]

numbers = list(map(int, input().split()))

numbers[l-1:r] = numbers[l-1:r][::-1]
print(*numbers)