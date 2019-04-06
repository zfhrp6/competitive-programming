n = int(input())
matrix = []
for _ in range(n):
    matrix.append(input())

for y in range(n):
    for x in range(n):
        print(matrix[n-1-x][y], end='')
    print()
