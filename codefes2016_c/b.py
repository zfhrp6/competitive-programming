K, T = list(map(int, input().split()))
a = list(map(int, input().split()))

# def remax(seq):
#     m = max(seq)
#     for idx,i in enumerate(seq):
#         if m==i:
#             return (idx, m)
#
# lastK = -1
# cnt = 0
# for _k in range(K):
#     remax
#

print(max(0,max(a)*2-sum(a)-1))
