def next_start(S, F):
    for i in range(S, S + F + 1):
        if i % F == 0:
            return i


N = int(input())
Cs, Ss, Fs = [], [], []

for i in range(N - 1):
    tmp = list(map(int, input().split()))
    Cs.append(tmp[0])
    Ss.append(tmp[1])
    Fs.append(tmp[2])


for nth in range(N - 1):
    t = 0
    for i in range(nth, N - 1):
        # print(i, nth, t)
        t = max(Ss[i], next_start(t, Fs[i]))
        # print('\t\t', i, nth, t)
        t += Cs[i]
        # print('\t', i, nth, t)
    print(t)
print(0)
