

def calc(N, K, seq):
    if N == 0:
        return 0
    if K >= 2 * N:
        return sum(filter(lambda x:x>0, seq))
    ans = 0
    for lcnt in range(0, K+1):
        tmpl = lget(N, lcnt, seq)
        tmpr = rget(N, K-lcnt, seq, tmpl[1])
        ans = max(ans, tmpl[0] + tmpr)
        print('ans, tmpk lcnt, rcnt: ', ans, tmpl[0] + tmpr, lcnt, K-lcnt)
        print()
    return ans



def lget(N, K, seq):
    """
    左からコストKで取ったときのスコア,どこまで取れるか
    非負の要素を取るときコストは1,負は2
    """
    got = []
    for idx,e in enumerate(seq):
        if K <= 0:
            break
        if N <= idx:
            break
        if e < 0:
            if K == 1:
                break
            K -= 2
        else:
            K -= 1
        got.append(e)
        print('l: ', N, K, idx, e, got)
    return sum(filter(lambda x:x>0, got)), idx

def rget(N, K, seq, lcount):
    '''
    右からコストKで取ったときのスコア
    非負の要素を取るときコストは1,負は2
    '''
    seq = list(reversed(seq))
    got, indx = [], 0
    for idx, e in enumerate(seq):
        if K <= 0:
            break
        if N - lcount <= idx:
            break
        if e < 0:
            if K == 1:
                break
            K -= 2
        else:
            K -= 1
        got.append(e)
        print('r: ', N, K, idx, e, got)
    return sum(filter(lambda x:x>0, got))

def main():
    N, K = list(map(int, input().split()))
    Vs = list(map(int, input().split()))
    print(calc(N, K, Vs))


if __name__ == '__main__':
    main()
