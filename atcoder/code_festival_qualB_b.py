# coding: utf-8

n,k = list(map(int,input().split(' ')))

s = 0
for i in range(1,n+1):
    s+=int(input())
    if s>=k:
        print(i)
        break