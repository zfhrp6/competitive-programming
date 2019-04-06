



# def test():
#     2 2/3
#     0 1
#     0 0



# def main():
#     i = input().split()
#     N,P = int(i[0]), int(i[1].split()[0])/int(i[1].split()[1])
#     A = {}
#     for row in range(1,N+1):
#         line = list(map(int, input().split()))
#         for col in range(1, N+1):
#             A[(row, col)] = line[col-1]


def main():
    i = input().split()
    N,P = int(i[0]), int(i[1].split('/')[0])/int(i[1].split('/')[1])
    A = {}
    for row in range(1,N+1):
        line = list(map(int, input().split()))
        for col in range(1, N+1):
            A[(row, col)] = line[col-1]
    if P==1:
        print(float(1))
        return
    elif P==0:
        print(float(0))
        return
    win_num = {}
    for i in range(1,N+1):
        tmp = 0
        for j in range(1, N+1):
            if A[(i,j)]==1:
                tmp += 1
        win_num[i] = tmp
    print(win_num)




if __name__ == '__main__':
    # test()
    main()
