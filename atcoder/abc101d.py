def take_n_snuke(n):
    ret = []
    m = (n - 1) // 9
    for x in range(m + 1):
        for topdigit in range(1, 10):
            ret.append(str(topdigit) + '9' * x)
    return ret


K = int(input())

for elm in take_n_snuke(K)[:K]:
    print(elm)
