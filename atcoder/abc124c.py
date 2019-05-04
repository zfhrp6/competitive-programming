S = input()
leng = len(S)

def make_valid(leng):
    s0 = ''
    s1 = ''
    last0 = '0'
    last1 = '1'
    for i in range(leng):
        s0 = s0 + last0
        s1 = s1 + last1
        last0, last1 = last1, last0
    return (s0, s1)


def count_dif(s, s1):
    ret = 0
    for idx,c in enumerate(s):
        if c != s1[idx]:
            ret += 1
    return ret

v0,v1 = make_valid(leng)
min_dif = min(count_dif(S,v0), count_dif(S,v1))
print(min_dif)
