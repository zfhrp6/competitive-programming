class NiceTable:
    def isNice(self, t):
        leng = (len(t), len(t[0]))
        flag = False
        for _x in range(2**leng[0]):
            for _y in range(2**leng[1]):
                x,y = bin(_x)[2:].zfill(leng[0]), bin(_y)[2:].zfill(leng[1])
                flag = True
                for i in range(leng[0]):
                    for j in range(leng[1]):
                        print(x,y,leng,t,'h')
                        if t[i][j]>0 and 1==x[i]^y[j]:
                            flag = False * flag
                        elif t[i][j]<1 and 0==x[i]^y[j]:
                            flag = False * flag
                        else:
                            flag = True * flag
                if flag:
                    return 'Nice'
        return 'Not nice'
