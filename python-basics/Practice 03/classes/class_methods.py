s = input()

change = 0
count = 0
for i in range(len(s)):
    if s[i]=='1':
        if change>count:
            count = change
            change = 0
    else:
        if s[i]=='0':
            change+=1

print(count)     
#100100010000