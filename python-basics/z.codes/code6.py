import re
s = input()
symbol = input()
tag = (symbol)
res = re.findall(tag, s)
print(res)



'''
import re

s = input()
tag = r"\d{2}/\d{2}/\d{4}"
res = re.findall(tag, s)

print(len(res))
'''



'''
import re
s = input()
pattern = r"Name: (.+), Age: (.+)"
match = re.search(pattern, s)

if match:
    name = match.group(1)
    age = match.group(2)
    print(f"{name} {age}")
'''

'''
import re

s = input()
p = input()
counter = 0
for i in range(len(s)):
    for j in range(len(p)):
        if p[j]==s[i]:
            counter += 1

print(counter)
'''