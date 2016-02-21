# coding: utf-8

n = int(input())
h_list = []
seeable = []
for i in range(n):
    h_list.append(int(input()))
    seeable.append(0)

h_list = tuple(h_list)
for idx,peek in enumerate(h_list):
    if idx == 0:
        for i in range(1,n):
            if h_list[i] > peek:
                break
            seeable[0] += 1
    elif h_list[idx-1] == peek:
        seeable[idx] = 0 + seeable[idx-1]
    elif h_list[idx-1] < peek:
        seeable[idx] += seeable[idx-1]
        for i in range(idx-seeable[idx-1]-1, -1, -1):
            if h_list[i] > peek:
                break
            seeable[idx]+=1
        for i in range(idx+1, n):
            if h_list[i] > peek:
                break
            seeable[idx]+=1
    else:
        for i in range(idx-1, -1,-1):
            if h_list[i] > peek:
                break
            seeable[idx]+=1
        for i in range(idx+1, n):
            if h_list[i] > peek:
                break
            seeable[idx]+=1

for i in seeable:
    print(i)
