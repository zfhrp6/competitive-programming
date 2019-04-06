num_room, num_kyaku = list(map(int, input().split()))
capa = list(map(int, input().split()))
kyaku = list(map(int, input().split()))

room_yoyaku = [0] * num_room

if num_kyaku > num_room:
    print('NO')
elif sum(kyaku) > sum(capa):
    print('NO')
else:
    capa = list(sorted(capa,reverse=True))
    kyaku = list(sorted(kyaku,reverse=True))
    preserved = 0
    rmidx = 0
    for idx,_kyaku in enumerate(kyaku):
        if _kyaku>capa[idx]:
            print('NO')
            break
        if idx==len(kyaku)-1:
            print('YES')
    # if preserved == num_kyaku:
    #     print('YES')
    # else:
    #     print('NO')
    # print('YES')
