x, y, M = map(int, input().split())
x = int('1'*x)
y = int('1'*y)

def gcd(a, b):
    if b==0: return a
    print('\tgcd:', a, b)
    return gcd(b, a%b)

def lcm(a, b):
    print('\tlcm:', a, b)
    return a*b//gcd(a, b)

print('gcd:', gcd(x, y))
print('lcm:', lcm(x, y))
print(lcm(x, y)%M)
