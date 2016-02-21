# coding: utf-8
ab = input().split(' ')
na = int(ab[0])
nb = int(ab[1])
# (na, nb) = list(map(int,input().spilt(' ')))
a_s = set(map(int, input().split(' ')))
b_s = set(map(int, input().split(' ')))

print(len(a_s & b_s) / len(a_s | b_s))