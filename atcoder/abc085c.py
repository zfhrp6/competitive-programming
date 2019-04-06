def gen_range(N, Y, reverse=False):
    for i in range(N, 0 - 1, -1):
        for j in range(N - i + 1):
            if reverse:
                yield (j, i, N - i - j)
            else:
                yield (i, j, N - j - i)


def calc(N, Y):
    if 10000 * N < Y or Y < 1000 * N:
        return [-1, -1, -1]
    if Y % 10000 == 0 and Y // 10000 == N:
        return (Y // 10000, 0, 0)
    if Y % 5000 == 0 and Y // 5000 == N:
        return (0, Y // 5000, 0)
    if Y % 1000 == 0 and Y // 1000 == N:
        return (0, 0, Y // 1000)
    if (Y - 1000 * N) % 4000 == 0:
        k5 = (Y - 1000 * N) // 4000
        if k5 >= 0 and N - k5 >= 0:
            return [0, k5, N - k5]
    elif (Y - 1000 * N) % 9000 == 0:
        k10 = (Y - 1000 * N) // 9000
        if k10 >= 0 and N - k10 >= 0:
            return [k10, 0, N - k10]
    if 5000 * N < Y:
        for k10, k1, k5 in gen_range(N, Y, reverse=True):
            if k10 * 10000 + k1 * 1000 + k5 * 5000 == Y:
                return (k10, k5, k1)
    else:
        for k10, k1, k5 in gen_range(N, Y):
            if k10 * 10000 + k1 * 1000 + k5 * 5000 == Y:
                return (k10, k5, k1)

    #
    # for k1 in range(N, 0 - 1, -1):
    #     for k10 in range(N - k1 + 1):
    #         if k1 * 1000 + k10 * 10000 > Y:
    #             break
    #         for k5 in range(N - k1 - k10 + 1):
    #             print(k10, k5, k1)
    #             if k1 * 1000 + k5 * 5000 + k10 * 10000 == Y:
    #                 return [k10, k5, k1]
    return (-1, -1, -1)


def main():
    N, Y = list(map(int, input().split()))
    print(*calc(N, Y))


if __name__ == '__main__':
    main()
