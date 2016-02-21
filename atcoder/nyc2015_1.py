# n = int(input())


def d2b(n):
    ret = []
    while n > 0:
        if n % 2:
            ret.append(1)
        else:
            ret.append(0)
        n = n // 2
    return ret


def isrev(seq):
    return seq[::-1] == seq[:]


def main():
    n = int(input())
    print('Yes' if isrev(d2b(n)) else 'No')

if __name__ == '__main__':
    main()
# print(d2b(2015))


# print(int(n,2))
