n = int(input())

i = 0
surnames = []
while i < n:
    surnames.append(input())
    i += 1

count = n
for i in range(len(surnames)):
    for j in range(len(surnames)-1, i, -1):
        if surnames[i]==surnames[j]:
            count -= 1
            surnames.pop(j)


print(count)