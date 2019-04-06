from read import read

def meminc(mem, val):
    if val in mem:
        mem[val] += 1
    else:
        mem[val] = 1


def calc(jpsk, mem):
    ret = 0
    available = []
    J, P, S, K = map(int, jpsk.split())
    for _s in range(1,S+1):
        for _p in range(1,P+1):
            for _j in range(1,J+1):
    # for _j in range(J,0,-1):
    #     for _p in range(P,0,-1):
    #         for _s in range(S,0,-1):
                jp = 'j{}p{}'.format(_j,_p)
                js = 'j{}s{}'.format(_j,_s)
                ps = 'p{}s{}'.format(_p,_s)
                jps = 'j{}p{}s{}'.format(_j,_p,_s)
                if jps in mem:
                    continue
                if (jp in mem and mem[jp]>=K) or (js in mem and mem[js]>=K) or (ps in mem and mem[ps]>=K):
                    continue
                ret += 1
                meminc(mem, jp)
                meminc(mem, js)
                meminc(mem, ps)
                meminc(mem, jps)
                available.append(' '.join(map(str, (_j,_p,_s))))
    # print(mem)
    rret = str(ret) + '\n'
    rret += '\n'.join(available)
    return rret


def main():
    import sys
    infile = read(sys.argv[1])
    outfilename = sys.argv[2]
    def it():
        return next(infile)

    T = int(it())

    with open(outfilename, 'w') as outfile:
        for caseidx in range(1, T+1):
            mem = {}
            jpsk = it()
            ans = calc(jpsk, mem)
            outfile.write('Case #{}: {}\n'.format(caseidx, ans))
            print('Case #{}: {}'.format(caseidx, ans))


if __name__ == '__main__':
    main()
