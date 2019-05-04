import sys

def flip(seg, idx):
    if idx == 0:
        return [sum(seg[0:3])] + seg[3:]
    if idx == len(seg) - 1:
        return seg[0:-3] + [sum(seg[-3:])]
    lseg = seg[:max(idx-2,0)] + [sum(seg[max(idx-2,0):idx])] + seg[idx+1:]
    rseg = seg[:idx] + [sum(seg[idx:min(idx+2,len(seg))])] + seg[min(idx+2,len(seg)):]
    if max(lseg) > max(rseg):
        return lseg
    else:
        return rseg

N, K = list(map(int, input().split()))
S = input()

segment_leng = []
last_c = 'X'
cnt = 0
for c in S:
    if last_c == 'X':
        last_c = c
        cnt += 1
        continue
    if last_c == c:
        cnt += 1
    else:
        last_c = c
        segment_leng.append(cnt)
        cnt = 1
segment_leng.append(cnt)

if K >= len(segment_leng) + 1:
    print(N)
    sys.exit()

tmp_seg = segment_leng
for iope in range(K):
    if len(tmp_seg) <= 1:
        print(max(tmp_seg))
        sys.exit()
    tmp_seg = flip(tmp_seg, tmp_seg.index(max(tmp_seg)))
print(max(tmp_seg))
