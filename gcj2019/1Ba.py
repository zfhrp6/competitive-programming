class Manhattan:
    def __init__(self, size):
        self.size = size
        self.field = [[0] * size[0]] * size[1]
        self.width = size[0]
        self.height = size[1]
        self.colmax = [0] * size[0]
        self.rowmax = [0] * size[1]

    def update(self, cood, dr):
        px, py = cood[0], cood[1]
        if dr == 'W':
            for x in range(px):
                self.field[0][x] = 1
                self.field[-1][x] = -1
        if dr == 'E':
            for x in range(px, self.size[0]):
                self.field[0][x] = 1
                self.field[-1][x] = -1
        if dr == 'N':
            for y in range(py, self.size[1]):
                self.field[y][0] = 1
                self.field[y][-1] = -1
        if dr == 'S':
            for y in range(py):
                self.field[y][0] = 1
                self.field[y][-1] = -1

    def update_max(self):
        for c in range(self.width):
            self.colmax[c] = max([self.field[r][c] for r in range(self.height)])
        for r in range(self.height):
            self.rowmax[r] = max([self.field[r][c] for c in range(self.width)])

    def get_max_field(self):




def answer_print(caseidx, answer_cood):
    print('Case #{}: {} {}'.format(caseidx, answer_cood[0], answer_cood[1]))


def calc(P, Q):
    minx, miny = 0, 0
    maxx, maxy = Q, Q
    for p in range(P):
        _p = input().split()
        px, py, dr = int(_p[0]), int(_p[1]), _p[2]
        if dr == 'W':
            maxx = min(px-1, maxx)
        if dr == "S":
            maxy = min(py-1, maxy)
        if dr == 'N':
            miny = max(py+1, miny)
        if dr == 'E':
            minx = max(px+1, minx)
    return (minx, miny)


def main():
    T = int(input())
    for t in range(1, T+1):
        P, Q = list(map(int, input().split()))
        ans = calc(P, Q)
        answer_print(t, ans)

if __name__ == '__main__':
    main()
