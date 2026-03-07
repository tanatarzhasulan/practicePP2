''' 501 code
import re

n = input()
if re.match(r"Hello", n):
    print('Yes')
else:
    print('No')
'''
'''
import re
s = input()
p = input()

if re.search(p, s):
    print('Yes')
else:
    print('No')
    '''

import re

s = input()
tag = r"\w+"
res = re.findall(tag, s)
print(len(res))