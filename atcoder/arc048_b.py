n = int(input())
men = []
rslt = []


jdic = [[0]*4 for _ in range(100001)]
cnt_d = [0] * 100001
lose_cnt_d = [0] * 100001
win_cnt_d = [0] * 100001


for _ in range(n):
    this_man = list(map(int , input().split()))
    jdic[this_man[0]][this_man[1]] += 1
    # if this_man[0] in jdic.keys():
    #     if this_man[1] in jdic[this_man[0]].keys():
    #         jdic[this_man[0]][this_man[1]] += 1
    #     else:
    #         jdic[this_man[0]][this_man[1]] = 1
    cnt_d[this_man[0]] += 1
    # else:
    #     u,uu = md(this_man[1]+1,3), md(this_man[1]+2,3)
    #     jdic[this_man[0]] = {u:0, uu:0, this_man[1]: 1}
    #     cnt_d[this_man[0]] = 1
    men.append(this_man)

# for idx,i in enumerate(cnt_d):
#     if i>0:
#         print(idx, i)

rate_s = 0
# keys = sorted(men)
keys = sorted(list(set([x[0] for x in men])))
# for r in keys[::-1]:
#     lose_cnt_d[r] = rate_s
#     rate_s += cnt_d[r]
rate_s = 0
for r in keys:
    win_cnt_d[r] = rate_s
    rate_s += cnt_d[r]

def g(num):
    if num == 1:
        return (2, 3, 1)
    if num == 2:
        return (3, 1, 2)
    else:
        return (1, 2, 3)

for man in men:
    mj = g(man[1])
    w,l,d = jdic[man[0]][mj[0]], jdic[man[0]][mj[1]], jdic[man[0]][mj[2]]
    # print("jdic", jdic)
    # print("lose", lose_cnt_d)
    # print("win", win_cnt_d)
    # print(w,l,d)
    print(' '.join(map(str, [win_cnt_d[man[0]] + w, n-win_cnt_d[man[0]]-cnt_d[man[0]] + l, d-1])))
# print(win_cnt_d)
