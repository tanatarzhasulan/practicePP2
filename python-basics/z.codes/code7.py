import re

def double(s):
    result = []
    for i in range(len(s)):
        r = s[i] * 2
        result = re.sub(s[i], r, s)
    print(result)

d = input()
double(d)

'''
def only_digits(s):
    pattern = re.compile(r"^\d*$")
    if pattern.fullmatch(s):
        print("Match")
    else:
        print("No match")

a = input()
only_digits(a)
'''

'''
def word_count(s):
    tag = r"\w+"
    result = re.findall(tag, s)
    if result:
        print(len(result))

a = input()
word_count(a)
'''

'''
def dig_more2(s):
    tag = r"\d{2,}"
    result = re.findall(tag, s)
    if result:
        print(*result)
    else:
        print()

a = input()
dig_more2(a)
'''

'''
def upper(s):
    tag = r"[A-Z]"
    result = re.findall(tag, s)
    print(len(result))

a = input()
upper(a)
'''

''' 510 code
def cat_dog(s):
    pattern = r"cat|dog"
    result = re.search(pattern, s)
    if result:
        print("Yes")
    else:
        print("No")

a = input()
cat_dog(a)
'''

'''
def length_3(s):
    tag = r"\b\w{3}\b"
    p = re.findall(tag, s)
    print(len(p))

a = input()
length_3(a)
'''    

'''
s = input()
d = input()
new = re.split(d, s)
print(*new, sep=",")
'''
'''
s = list(input().split())
p = input()
r = input()
for i in range(len(s)):
    if s[i]==p:
        s[i] = r
print(*s)
'''

'''
def text_email(s):
    tag = r"\S+@\S+\.\S+"
    p = re.search(tag, s)
    if p:
        print(p.group())
    else:
        print("No email")

a = input()
text_email(a)
'''
'''
def letter_dig(s):
    tag = r"^[a-zA-Z].*[0-9]$"
    if re.fullmatch(tag, s):
        print("Yes")
    else:
        print("No")


s = input()
letter_dig(s)
'''