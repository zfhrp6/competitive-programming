N = input()
SN = sum(map(int, list(N)))
print('Yes' if int(N) % SN == 0 else 'No')
