
mem = {}
def per(a, b):
    pass

def maxperm(a, b):
    return bin(int('1'*a + '0'*b, 2))

def minperm(a, b):
    ret = ''
    for _ in range(b):
        ret += '10'
    ret += '1'*(a-b)
    return bin(int(ret, 2))

def main():
    A, B = map(int, raw_input().split())
    print(
    maxperm(A, B),
    minperm(A, B))
    print(int(maxperm(A, B), 2)-int(minperm(A, B),2))


if __name__ == '__main__':
    main()
