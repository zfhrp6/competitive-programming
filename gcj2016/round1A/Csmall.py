from read import read
import networkx as nx


def calc(sts):
    tmpd = {}           # student to student graph ( one -> BFF )a
    num_students = len(sts)
    # for _ in range(len(sts)):
    #     tmpd[_+1] = []
    for idx,to_id in enumerate(sts):
        from_id = idx+1
        tmpd[from_id] = to_id
    digra = nx.DiGraph()
    digra.add_edges_from(tmpd.items())
    gra = nx.Graph()
    gra.add_edges_from(tmpd.items())
    print(sts)
    lgra = list(nx.connected_components(gra))
    ldigra = list(nx.strongly_connected_components(digra))
    print(lgra)
    print(ldigra)
    tar = sorted(lgra, key=lambda x:len(x))
    ditar = sorted(ldigra, key=lambda x:len(x))

    ret = 0
    edgs = digra.edges()
    cycles = list(filter(lambda x:len(x)>2, ditar))
    pairs = list(filter(lambda x:len(x)==2, ditar))
    # for i in ditar:
    #     for j in ditar:
    #         # print(i,j)
    #         if i==j:
    #             continue
    #         try:
    #             lenpath = nx.dijkstra_path(source=i, target=j, G=digra)
    #         except:
    #             lenpath = []
    #         # print('l',lenpath)
    #         if not lenpath is False and ret < len(lenpath):
    #             if (lenpath[-1], lenpath[0]) in edgs:
    #                 lenpath
    #             ret = len(lenpath)
    #             maxpath = lenpath

    pairs_sur = []
    for pair in pairs:
        to_pair_path = [list(pair)[0], list(pair)[1]]
        maxtoheadpath = []
        maxtotailpath = []
        for i in range(1, num_students+1):
            if i in to_pair_path:
                continue
            try:
                toheadpath = nx.dijkstra_path(source=i, target=to_pair_path[0], G=digra)
                if len(maxtoheadpath) < len(toheadpath) and to_pair_path[1] not in toheadpath:
                    maxtoheadpath = toheadpath
            except nx.exception.NetworkXNoPath as e:
                pass
            try:
                totailpath = nx.dijkstra_path(source=i, target=to_pair_path[1], G=digra)
                if len(maxtotailpath) < len(totailpath) and to_pair_path[0] not in totailpath:
                    maxtotailpath = totailpath
            except nx.exception.NetworkXNoPath as e:
                pass
        if maxtoheadpath != []:
            to_pair_path = maxtoheadpath + to_pair_path[1:]
        if maxtotailpath != []:
            to_pair_path = to_pair_path[:-1] + maxtotailpath[::-1]
        pairs_sur = pairs_sur + to_pair_path
    # for i in tar:
    #     if not i in maxpath and len(ditar) == 2:
    #         if (i, maxpath[0]) in edgs:
    #         elif (i, maxpath[1]) in edgs:
    #         ret += 1
    #         break
    print(cycles)
    print('pairss', pairs_sur)
    # print(maxpath)
    if len(cycles) > 0 and len(pairs_sur) < len(cycles[-1]):
        return len(cycles[-1])
    else:
        return len(pairs_sur)
    return ret


def main():
    import sys
    infile = read(sys.argv[1])
    outfilename = sys.argv[2]
    def it():
        return next(infile)

    T = int(it())   # case number

    with open(outfilename, 'w') as outfile:
        for caseidx in range(1, T+1):
            # input('aaa')
            # input()                 #debugggggggggggggggggggggggggggg
            N = int(it())
            # print('N: {}'.format(N)) # debuggggggggggggggggggggggggggggg
            students = list(map(int, it().split()))
            ans = calc(students)
            outfile.write('Case #{}: {}\n'.format(caseidx, ans))
            print('Case #{}: {}'.format(caseidx, ans))


if __name__ == '__main__':
    main()
