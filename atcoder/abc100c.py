N = int(input())
a = list(map(int, input().split()))


def div2count(num):
    ret = 0
    while num % 2 == 0:
        ret += 1
        num = num // 2
    return ret


print(sum(map(div2count, a)))
