c11, c12, c13 = list(map(int, input().split()))
c21, c22, c23 = list(map(int, input().split()))
c31, c32, c33 = list(map(int, input().split()))

print('Yes' if c11 - c21 == c12 - c22 == c13 - c23 and
      c21 - c31 == c22 - c32 == c23 - c33 and
      c31 - c11 == c32 - c12 == c33 - c13 and
      c11 - c12 == c21 - c22 == c31 - c32 and
      c12 - c13 == c22 - c23 == c32 - c33 and
      c13 - c11 == c23 - c21 == c33 - c31 else 'No')
