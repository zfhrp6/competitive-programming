

def main():
    n,a,b = list(map(int,input().split(' ')))
    ret = 0
    if(n>=5):
        ret += a*(n-5)
        ret += b*5
    else:
        ret += b*n
    print(ret)

if __name__ == '__main__':
    main()
