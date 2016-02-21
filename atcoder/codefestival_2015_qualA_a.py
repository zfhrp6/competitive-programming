import re

# aa = re.compile(r'2015$')

s = input()

ret = re.sub(r'2014$', '2015', s)
# aa.search(s)
print(ret)

