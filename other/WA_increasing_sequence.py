#! /usr/bin/env python2
# coding: utf-8
import itertools
import time
a, b = map(int, raw_input().split())
t0 = time.time()
def check(s):
    c = 0
    for i in s:
        c += 1 if i=='1' else -1
        if c<0:
            return False
    return True

ts = '1'*a + '0'*b
cnt = 0
debug = 0
used = []
for smpl in itertools.permutations(list(ts)):
    # print(''.join(smpl))
    aa = ''.join(smpl)
    if aa in used:
        continue
    used.append(aa)
    cnt += 1 if check(aa) else 0
    debug += 1
    if debug%100==0:
        print(debug)
f = lambda x:1 if not x else x*f(x-1)
print(a,b)
print(f(a))
print(cnt/(f(a)*f(b)))
print(time.time()-t0)
