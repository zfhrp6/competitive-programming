N = int(input())

A1, A2 = list(map(int, input().split())), list(map(int, input().split()))

print(max([sum(A1[:i + 1] + A2[i:]) for i in range(N)]))
