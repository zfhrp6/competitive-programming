def calc(n, m):
    if n == 1:
        if m == 1:
            return 1
        if m == 2:
            return 0
        if m >= 3:
            return m - 2
    elif n == 2:
        return 0
    else:
        if m == 1:
            return n - 2
        elif m == 2:
            return 0
        else:
            return (n - 2) * (m - 2)


def main():
    N, M = list(map(int, input().split()))
    print(calc(N, M))


if __name__ == '__main__':
    main()
