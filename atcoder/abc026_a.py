# coding:utf-8


a = int(input())
if (a%2):
    print(((a-1)//2)*((a-1)//2+1))
else:
    print((a//2)**2)
"""
10

出力例1

25

x=5, y=5 のとき、 x×y=25 となり、これが最大値となります。
入力例2

60

出力例2

900

"""