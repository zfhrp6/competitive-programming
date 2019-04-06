class Plate:
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def contains(self, plate):
        return self.h >= plate.h and self.w >= plate.w

N, H, W = list(map(int, input().split()))
need_plate = Plate(H, W)
plates = []


ret = 0
for i in range(N):
    if Plate(*list(map(int, input().split()))).contains(need_plate):
        ret += 1


print(ret)
