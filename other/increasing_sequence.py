#! /usr/bin/env python2
# coding: utf-8
MaxN = 30
mem = [[0 for _ in range(MaxN+1)] for _ in range(MaxN+1)]


def rmem(a, b):
    if b>a:
        return 0
    if mem[a][b] > 0:
        return mem[a][b]
    if b == 0:
        mem[a][b] = 1
        return 1
    elif b == 1:
        mem[a][b] = a
        return a
    seq1x = rmem(a-1, b)
    seq10x = rmem(a, b-1)
    ret = seq1x + seq10x
    mem[a][b] = ret
    return ret


def main():
    a, b = map(int, raw_input().split())
    print(rmem(a, b))


if __name__ == '__main__':
    main()

