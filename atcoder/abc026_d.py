# coding:utf-8

from math import sin
pi = 3.1415926535897932
a, b, c = [int(s) for s in input().split(' ')]


def f(t):
    return a * t + b * sin(c * t * pi)


def g(t):
    return f(t) - 100

itr = 100
itl = 0
ret = 0
while abs(g(ret)) > 0.0000001:
    # print(ret)
    if 1 or g(itl) * g(itr) < 0:
        if g(itl) * g((itr + itl) / 2) > 0:
            itl = (itl + itr) / 2
        else:
            itr = (itl + itr) / 2
    ret = (itl + itr) / 2
print(ret)
# print(f(0.7806844588230888))
# print(g(0.7806844588230888))

"""

f(t) = A*t + B*sin(C*t*pi)
t>=0 and f(t)==100

入力例1

1 1 1

出力例1

100

t=100 のとき、 f(t)=100 となります。
入力例2

53 82 49

出力例2

1.63372043395339

解が一つではないことに注意してください。

"""