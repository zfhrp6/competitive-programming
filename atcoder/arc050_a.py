c1, c2 = input().split()
if c1 == c2 or min(ord(c1), ord(c2))+32 == max(ord(c1), ord(c2)):
    print('Yes')
else:
    print('No')
