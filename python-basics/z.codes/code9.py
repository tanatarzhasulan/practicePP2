'''
n = int(input())
arr = list(map(int, input().split()))

summ = 0
for i in arr:
    summ += i*i

print(summ)
'''

"""
def even_num(x):
    counter = 0
    if x % 2 == 0:
        counter += 1
    return counter

n = int(input())
numbers = list(map(int, input().split()))

result = filter(even_num, numbers)
print(len(list(result)))
    
"""

'''
a = int(input())
s = list(input().split())

for index, val in enumerate(s):
    print(f"{index}:{val}", end = " ")
    '''

'''
n = int(input())
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

result = []
for a, b in zip(num1, num2):
    result.append(a*b)

print(sum(result))
'''

import re

text = input()
pattern = input()

escaped_pattern = re.escape(pattern)
matches = re.findall(escaped_pattern, text)
count = len(matches)

print(count)


