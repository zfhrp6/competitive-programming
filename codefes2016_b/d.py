N = int(input())
As = []
for _ in range(N):
    As.append(int(input()))

ans = 0
m_p = 1
for idx,a in enumerate(As):
    if As[idx] <= m_p:
        continue
    while As[idx] > m_p:
        ans += 1
        As[idx] -= m_p
    m_p = max(m_p, As[idx]+1)
print(ans)


'''
3 1-2
1 
4 2-1
1
5 3-1
9 3-2
2
6 4-1
5 4-1
3
5 4-1
8 4-1
9 4-1
7 5-1
9 5-1
'''
