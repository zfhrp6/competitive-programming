def check(s):
    tmp = 0
    leng = len(s)
    for idx,c in enumerate(s):
        if leng - idx < tmp:
            return False
        if c=='(':
            tmp += 1
        else:
            tmp -= 1
        if tmp < 0:
            return False
    if tmp == 0:
        return True
    return False


def repair(s):
    tmp = 0
    tmpidx = 0
    leng = len(s)
    ridx = [0]
    cnt = 0
    s = list(s)
    for idx,c in enumerate(s):
        if leng - idx <= tmp:
            if c=='(':
                ridx.append(idx)
                s[idx] = ')'
                cnt += 1
                tmp -= 1
            else:
                tmp -= 1
        else:
            if c=='(':
                tmp += 1
            else:
                tmp -= 1
        if tmp < 0:
            ridx.append(s.index(')'))
            s[s.index(')')] = '('
            cnt += 1
            tmp += 2
        # print(tmp)
    cnt += max(ridx)
    print('max:', max(ridx))
    return cnt,''.join(s)

def ch(s):
    tmp = 0
    leng = len(s)
    for idx,c in enumerate(s):
        if c=='(':
            tmp += 1
        else:
            tmp -= 1
        if tmp < 0:
            return -1,idx
    return 1,tmp


def r(s):
    return repair(s),check(s)


def t(s):
    print(len(s),r(s))

def p(s):
    print(len(s), cal(s))

def cal(s):
    s = list(s)
    return cali(s, 0, 0)

def cali(s, acm, maidx):
    if check(s):
        return acm
    aa = ch(s)
    if aa[0]<0:
        s[s.index(')')] = '('
        maidx = max(maidx, s.index(')'))
        acm += 1
        cali(s, acm, maidx)
    else:


    cali(ch(s)[1])

def test():
    # S = input()
    t('())(()))')   #2
    t('((((')       #5
    t(')))(((')     #9
    t(')((((((((()))))))))(')
    t('))))))))))')


def main():
    S = input()
    print(repair(S))


if __name__ == '__main__':
    # main()
    test()
