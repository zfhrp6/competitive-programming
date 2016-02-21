import sys
def read():
    return sys.stdin.readline().strip()

def main():
    ls = [1,2,3,4,5,6]
    n = int(read())
    m = n
    #while m>5:
    #    m = m//5
    while m>27000:
        m = m - 27000
    while m>900:
        m = m - 900
    while m>30:
        m = m - 30
    m = m//5
    ls = ls[m:]+ls[:m]
    #print(ls)
    n = n%5
    #print(n)
    for i in range(n):
        ls[i%5], ls[i%5+1] = ls[i%5+1], ls[i%5]
    print("".join(map(str,ls)))

if __name__ == '__main__':
    main()
