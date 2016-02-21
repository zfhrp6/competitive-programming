s = input()
n = int(input())

def rev(s,l,r):
    ll = s[:l-1]
    rr = s[r:]
    cc = s[l-1:r]
    cc = cc[::-1]
    return ll+cc+rr

for q in range(n):
    l,r = list(map(int, input().split(' ')))
    s = rev(s,l,r)

print(s)
