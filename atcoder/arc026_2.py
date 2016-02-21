from math import sqrt

def check(n):
    ret = 0
    for i in range(1,1+int(sqrt(n))):
        if n%i==0:
            ret += i + n//i
    if sqrt(n)%1 == 0.0:
        ret -= int(sqrt(n))
    return ret-n

def main():
    n = int(input())
##    n = i
    if n == check(n):
        print('Perfect')
    elif n > check(n):
        print('Deficient')
    else:
        print('Abundant')
##    print(check(n),n)

if __name__ == '__main__':
    main()
