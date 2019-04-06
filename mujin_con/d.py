def parenstr(st):
    if st=='':
        return True
    elif len(st) >= 2 and st[0]=='(' and st[-1]==')':
        return parenstr(st[1:-1])
    else:
        pass


def check(st):
    if len(st)==0:
        return True
    else:
        cnt = 0
        for c in st:
            cnt += (1 if c=='(' else -1)
            if cnt < 0:
                return False
    return True


def isenable(st):
    if len(st)==0:
        return True
    if len(st)%2 == 1:
        return False
    if st[-1] == '(' or st[0] == ')':
        return False
    q_cnt = 0
    cnt = 0
    for c in st:
        cnt += (1 if c=='(' else -1 if c==')' else 0)
        q_cnt += 1 if c=='?' else 0
        if cnt < 0 and (cnt + q_cnt) < 0:
            return False
    if cnt - q_cnt > 0:
        return False
    if cnt == 0 or cnt - q_cnt <= 0:
        return True
    else:
        return False


def main():
    N = int(input())
    S = input()
    Qnum = int(input())
    Qs = []
    for i in range(Qnum):
        l,r = map(int, input().split())
        si = S[l-1:r]
        print('Yes' if isenable(si) else 'No')
        # if (r-l-1) % 2 == 1:
        #     print('No')
        # else:
        #
        #     pass


if __name__ == '__main__':
    main()

