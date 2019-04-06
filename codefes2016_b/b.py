N, A, B = list(map(int, input().split()))
S = input()
a_cnt = 0
b_cnt = 0
ab_cnt = 0

for c in S:
    if c == 'a':
        if ab_cnt < A+B:
            print('Yes')
            a_cnt += 1
            ab_cnt += 1
        else:
            print('No')
    elif c == 'b':
        if ab_cnt < A+B and b_cnt < B:
            print('Yes')
            b_cnt += 1
            ab_cnt += 1
        else:
            print('No')
    else:
        print('No')
