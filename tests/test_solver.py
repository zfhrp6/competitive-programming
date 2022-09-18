import unittest

from solver import Board, Coord

TEST_BOARD_INPUT = '''13 24
14 24
15 24
16 24
17 24
12 23
18 23
11 22
19 22
10 21
20 21
9 20
21 20
8 19
15 19
18 19
22 19
8 18
12 18
15 18
18 18
22 18
8 17
12 17
15 17
18 17
22 17
8 16
12 16
15 16
18 16
22 16
8 15
12 15
15 15
18 15
22 15
9 14
12 14
15 14
18 14
21 14
10 13
12 13
15 13
18 13
20 13
22 13
11 12
12 12
15 12
18 12
19 12
23 12
12 11
15 11
18 11
24 11'''

class TestSolver(unittest.TestCase):
    def initialize(self):
        n, m = 33, 58
        initial_points = []
        for line in TEST_BOARD_INPUT.split('\n'):
            # print(line)
            px, py = list(map(int, line.split()))
            initial_points.append(Coord(px, py))
        self.board = Board(n, initial_points)

    def test_get_line_points(self):
        self.initialize()
        x = sorted(self.board.get_line_points((9, 15), mode='x'))
        assert x == sorted([(22, 15), (12, 15), (18, 15), (8, 15), (15, 15)]), x
        y = sorted(self.board.get_line_points((9, 15), mode='y'))
        assert y == sorted([(9, 20), (9, 14)]), y
        up = sorted(self.board.get_line_points((9, 15), mode='up'))
        assert up == sorted([(12, 18)]), up
        down = sorted(self.board.get_line_points((9, 15), mode='down'))
        assert down == sorted([(12, 12), (8, 16)]), down
        all_ = sorted(self.board.get_line_points((9, 15), mode='all'))
        assert all_ == sorted([(22, 15), (8, 16), (12, 12), (9, 14), (12, 15), (18, 15), (12, 18), (8, 15), (9, 20), (15, 15)]), all_


if __name__ == '__main__':
    unittest.main()