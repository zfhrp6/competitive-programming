#! /usr/bin/env python2
# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N, L = map(int, raw_input().split())
a = []
current_leng = L
used_count = 1
for _ in range(N):
    # a.append(int(raw_input()))
    a_i = int(raw_input())
    if current_leng >= a_i:
        current_leng -= a_i
    else:
        current_leng = L - a_i
        used_count += 1
print(used_count)
