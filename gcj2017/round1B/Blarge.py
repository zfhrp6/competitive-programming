from read import read
from time import sleep
from multiprocessing import Process
from multiprocessing.managers import SyncManager

manager = SyncManager()
manager.start()
anss = manager.list()


def make1(s):
    ret = []
    for i in range(10):
        tmps = s.replace('?', str(i))
        ret.append(tmps)
    return ret

def make2(s):
    ret = []
    for i in range(10):
        tmps = s[:s.index('?')]+str(i)+s[s.index('?')+1:]
        for j in range(10):
            ret.append(tmps.replace('?', str(j)))
    return ret

def make3(s):
    ret = []
    for i in range(10):
        tmps = s[:s.index('?')] + str(i) + s[s.index('?')+1:]
        for j in range(10):
            tmpss = tmps[:tmps.index('?')] + str(j) + tmps[tmps.index('?')+1:]
            for k in range(10):
                ret.append(tmpss.replace('?', str(k)))
    return ret


def maken(s, n):
    ret = []
    tmp = [[s]]
    for qnum in range(n):
        t = []
        ss = tmp[qnum]
        for s in ss:
            for dig in range(10):
                tmps = s[:s.index('?')] + str(dig) + s[s.index('?')+1:]
                t.append(tmps)
            tmp.append(t)
    return tmp[-1]



def make(s, num):
    if num==1:
        return make1(s)
    if num==2:
        return make2(s)
    if num==3:
        return make3(s)
    if num==0:
        return [s]
    else:
        raise Exception


def calc(st):
    ret = ''
    coder, jammer = st.split()
    pcoder = maken(coder, coder.count('?'))
    pjammer = maken(jammer, jammer.count('?'))
    # print(st,pcoder,pjammer)
    mdiff = [99999, ('99999','99999')]
    for cscore in pcoder:
        for jscore in pjammer:
            di = abs(int(cscore)-int(jscore))
            if di == mdiff[0]:
                if (cscore == mdiff[1][0] and jscore < mdiff[1][1]) or cscore < mdiff[1][0]:
                    mdiff[0] = di
                    mdiff[1] = (cscore, jscore)
            elif di < mdiff[0]:
                mdiff[0] = di
                mdiff[1] = (cscore, jscore)
    # for c in st:
    #     if ret == '':
    #         ret += c
    #     elif c >= ret[0]:
    #         ret = c + ret
    #     else:
    #         ret = ret + c
    ret = ' '.join(mdiff[1])
    return ret


def multicalc(caseidx, st, ls):
    ls.append((caseidx, calc(st)))


def main():
    import sys
    infile = read(sys.argv[1])
    outfilename = sys.argv[2]
    def it():
        return next(infile)

    T = int(it())

    with open(outfilename, 'w') as outfile:
        prss = []
        for caseidx in range(1, T+1):
            sleep(0.03)
            S = it()
            prss.append(Process(target=multicalc, kwargs={'caseidx':caseidx, 'st':S, 'ls':anss}))
            prss[-1].start()
        for p in prss:
            p.join()
        for a in sorted(anss):
            caseidx = a[0]
            ans = a[1]
            outfile.write('Case #{}: {}\n'.format(caseidx, ans))
            print('Case #{}: {}'.format(caseidx, ans))


if __name__ == '__main__':
    main()
