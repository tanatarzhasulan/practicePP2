s = input()

cha = 0
for i in range(1, len(s)):
    if s[i-1]==s[i]:
        cha += 1
print(cha)