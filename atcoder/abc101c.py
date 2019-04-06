N, K = list(map(int, input().split()))
As = list(map(int, input().split()))


def calc(n, k, As):
    from math import ceil
    if k >= n:
        return 1
    return ceil((n - 1) / (k - 1))


print(calc(N, K, As))
