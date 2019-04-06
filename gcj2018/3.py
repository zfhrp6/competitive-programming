import sys


def read_i_j():
    I, J = list(map(int, input().split()))
    if I == J == 0 or I == J == -1:
        sys.exit()


def send_x_y(x, y):
    sys.stdout.write('{} {}'.format(x, y))
    sys.stdout.flush()


def calc_cover_size(a):
    for i in range(a):
        if 3 * i >= a:
            return (i, 3)


def init_test_area(size):
    dic = {}
    for x in range(1, 1 + size[0]):
        for y in range(1, 1 + size[1]):
            dic[(x, y)] = 1
    return dic


def test_calc():
    A = int(input())
    min_size = calc_cover_size(A)
    prepared_dic = init_test_area(min_size)
    pass


def main():
    T = int(input())
    for tidx in range(1, T + 1):
        ans = test_calc()


if __name__ == '__main__':
    main()
