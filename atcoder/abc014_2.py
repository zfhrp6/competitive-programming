print(sum(map((lambda xy:xy[0]*xy[1]),zip(map(int,reversed(bin(int(input().split(
)[1]))[2:])),map(int,input().split())))))