N = int(input())
def calc(N):
    if len(str(N)) == 1:
        return N
    if len(list(set(str(N)[1:]))) == 1 and '9' in  list(set(str(N)[1:])):
        return int(str(N)[0])+9*len(str(N)[1:])
    ret = 0
    f = 0
    for idx,c in enumerate(str(N)):
        tmp = int(c)
        if f == 1:
            ret += 9
            continue
        if tmp != 9 and idx == 0:
            ret += tmp-1
            f = 1
            continue
        elif tmp != 9:
            ret -= 1
            f = 1
            ret += 9
            continue
        else:
            ret += 9
            continue
    return ret
print(calc(N))
