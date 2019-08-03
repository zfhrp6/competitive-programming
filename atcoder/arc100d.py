import bisect

def main():
    N = int(input())
    As = list(map(int, input().split()))
    ruiseki = []
    tmp = 0
    for e in As:
        tmp += e
        ruiseki.append(tmp)

    ans = tmp
    # first_separator は最初に半分に割る区切り(index番目の前に置くことにする)(0-origin indexの2の前が最小)
    for first_separator in range(2, N-1):
        d('fsep', first_separator)
        lseps = separate_seq(ruiseki, 0, first_separator)
        rseps = separate_seq(ruiseki, first_separator, N)
        for lsep in lseps:
            for rsep in rseps:
                if (lsep <= 0 or N <= rsep):
                    continue
                d('loop in', lsep,first_separator, rsep)
                s1 = sum_of_segment(ruiseki, 0, lsep)
                s2 = sum_of_segment(ruiseki, lsep, first_separator)
                s3 = sum_of_segment(ruiseki, first_separator, rsep)
                s4 = sum_of_segment(ruiseki, rsep, N)
                if min(s1, s2, s3, s4) <= 0:
                    d('error')
                    continue
                diff = max(s1, s2, s3, s4) - min(s1, s2, s3, s4)
                ans = min(diff, ans)
                d('ans', ans, 'diff', diff, 'sums', s1, s2, s3, s4, 'seps', lsep, first_separator, rsep)
    print(ans)

def d(*args):
    # print(*args)
    pass


def separate_seq(seq, l, r):
    d('ss in', seq, l, r)
    S = (seq[l] + seq[r-1])/2
    ret = []
    lidx = bisect.bisect_left(seq, S)
    ret.append(lidx-1)
    ret.append(lidx)
    ret.append(lidx+1)
    d('ss out', seq, l, r, 'S', S, 'ret', ret, lidx)
    return ret


def sum_of_segment(seq, start, end):
    # d('sos in', start, end)
    ret = seq[0]
    if start == 0:
        ret = seq[end-1]
    elif end-1 != 0:
        ret = seq[end-1] - seq[max(start-1, 0)]
    # d('sos out', seq, start, end, ret)
    return ret

main()