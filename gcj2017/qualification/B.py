from read import read

def check(s_num):
    return list(s_num) == sorted(list(s_num))


def when(s_num):
    lc = 9
    for c in s_num:
        if int(c)

def calc2(num):
    for x in range(int(num), 0-1, -1):
        if check(str(x)):
            ret = x
            break
    return ret

def flip(seq, i):
    ret = ''
    for c in reversed(seq[:i]):
        ret += '+' if c == '-' else '-'
    for c in seq[i:]:
        ret += c
    return ret


def main():
    import sys
    infile = read(sys.argv[1])
    outfilename = sys.argv[2]
    def it():
        return next(infile)

    mem = {}
    N = int(it())

    with open(outfilename, 'w') as outfile:
        for caseidx in range(1, N+1):
            inputline = it()
            ans = calc2(inputline.strip())
            outfile.write('Case #{}: {}'.format(caseidx, ans))
            outfile.write('\n')
            print('{} -> Case #{}: {}'.format(inputline, caseidx, ans))


if __name__ == '__main__':
    main()
