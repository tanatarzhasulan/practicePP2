import re

def name_age(s):
    pattern1 = r"([a-zA-Z]+)[,\s]*"
    name = re.search(pattern1, s)
    pattern = r"\d+"
    age = re.search(pattern, s)
    print(name.group(), age.group())

s = input()
name_age(s)