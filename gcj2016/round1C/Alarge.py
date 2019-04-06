from read import read


def s(n):
    return chr(65+n)


def calc(N, st):
    ret = ''
    N = int(N)
    st = list(map(int, st.split()))
    orgst = st[:]
    p_sum = sum(st)
    cnt = 0
    while cnt < p_sum:
        mx = max(st)
        if p_sum - cnt == 3:
            tmp = ''
            for idx,p in enumerate(st):
                if p > 0:
                    tmp += s(idx)
            # print(orgst,tmp)
            ret += '{} {}{}'.format(tmp[0],tmp[1],tmp[2])
            cnt += 3
            break
        for idx,p in enumerate(st):
            if p == mx:
                st[idx] -= 1
                ret += s(idx)
                cnt += 1
                if cnt % 2==0:
                    ret += ' '
                break
        for idx,p in enumerate(st):
            if p == mx:
                st[idx] -= 1
                ret += s(idx)
                cnt += 1
                if cnt % 2==0:
                    ret += ' '
                break

    return ret


def main():
    import sys
    infile = read(sys.argv[1])
    outfilename = sys.argv[2]
    def it():
        return next(infile)

    T = int(it())

    with open(outfilename, 'w') as outfile:
        for caseidx in range(1, T+1):
            N = it()
            ps = it()
            ans = calc(N, ps)
            outfile.write('Case #{}: {}\n'.format(caseidx, ans))
            print('Case #{}: {}'.format(caseidx, ans))


if __name__ == '__main__':
    main()
