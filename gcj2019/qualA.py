def output(case_number, ans_tuple):
    print('Case #{case_number}: {a0} {a1}'.format(case_number=case_number,a0=ans_tuple[0],a1=ans_tuple[1]))


def calc(n):
    if '4' not in str(n):
        return (n, 0)

    ret1,ret2 = n,0
    for idx, c in enumerate(reversed(str(n))):
        if c == '4':
            ret1 -= 1 * 10**idx
            ret2 += 1 * 10**idx
    return (ret1, ret2)


def main():
    T = int(input())
    for case_idx in range(1,T+1):
        N = int(input())
        output(case_idx, calc(N))



if __name__ == '__main__':
    main()
