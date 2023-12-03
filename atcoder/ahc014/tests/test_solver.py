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


class TestSolver:
    def setup_method(self):
        self.initialize()

    def initialize(self):
        n, m = 33, 58
        initial_points = []
        for line in TEST_BOARD_INPUT.split('\n'):
            # print(line)
            px, py = list(map(int, line.split()))
            initial_points.append(Coord(px, py))
        self.board = Board(n, initial_points)

    def test_board_weight(self):
        w = self.board.board_weight
        assert w == 198561, w

    def test_get_line_points_x(self):
        x = self.board.get_line_points(Coord(12, 18), mode='x')
        x = list(sorted(x))
        assert x == [(8, 18), (15, 18)], x

    def test_get_line_points_y(self):
        y = self.board.get_line_points(Coord(15, 18), mode='y')
        y = list(sorted(y))
        assert y == sorted([(15, 17), (15, 19)]), y

    def test_get_line_points_up(self):
        up = self.board.get_line_points(Coord(12, 18), mode='up')
        up = list(sorted(up))
        assert up == [], up

    def test_get_line_points_down(self):
        down = self.board.get_line_points(Coord(12, 18), mode='down')
        down = list(sorted(down))
        assert down == [(15, 15)], down

    def test_get_line_points_all(self):
        all_ = self.board.get_line_points(Coord(12, 18), mode='all')
        all_ = list(sorted(all_))
        assert all_ == sorted([(8, 18), (15, 18), (12, 17), (12, 23), (15, 15)]), all_

    def test_score(self):
        actual = self.board.score
        assert actual == 202641, actual

        self.board.choose(Coord(9, 15), tuple((Coord(12, 12), Coord(15, 15), Coord(12, 18))))

        actual = self.board.score
        assert actual == 207464, actual

    def test_search_candidates_from_point(self):
        x_y_expected = [
            ((12, 19), ((12, 18), (8, 18), (8, 19))),
            ((12, 19), ((12, 18), (15, 18), (15, 19))),
        ]
        y_x_expected = [
            # empty
        ]
        up_down_expected = [
            # empty
        ]
        down_up_expected = [
            ((9, 15), ((12, 18), (15, 15), (12, 12))),
            ((15, 21), ((12, 18), (15, 15), (18, 18))),
        ]

        candidates = list(sorted(self.board.search_candidate_choices_from_point(Coord(12, 18))))
        print('len', len(candidates))
        for c in candidates:
            print(c)
        assert candidates == sorted(x_y_expected + y_x_expected + up_down_expected + down_up_expected), candidates

    def test_is_vacancy(self):
        assert self.board.is_vacancy(Coord(9, 15), Coord(9, 15)) == False

        assert self.board.is_vacancy(Coord(9, 15), Coord(12, 15)) == True
        assert self.board.is_vacancy(Coord(9, 15), Coord(15, 15)) == False

        assert self.board.is_vacancy(Coord(9, 15), Coord(12, 18)) == True
        assert self.board.is_vacancy(Coord(9, 15), Coord(13, 19)) == False

        assert self.board.is_vacancy(Coord(9, 15), Coord(9, 20)) == True
        assert self.board.is_vacancy(Coord(9, 15), Coord(9, 21)) == False

        assert self.board.is_vacancy(Coord(9, 15), Coord(8, 16)) == True
        assert self.board.is_vacancy(Coord(9, 15), Coord(7, 17)) == False

        assert self.board.is_vacancy(Coord(9, 15), Coord(8, 15)) == True
        assert self.board.is_vacancy(Coord(9, 15), Coord(7, 15)) == False

        assert self.board.is_vacancy(Coord(9, 15), Coord(8, 14)) == True

        assert self.board.is_vacancy(Coord(9, 15), Coord(9, 14)) == True
        assert self.board.is_vacancy(Coord(9, 15), Coord(9, 13)) == False

        assert self.board.is_vacancy(Coord(9, 15), Coord(12, 12)) == True
        assert self.board.is_vacancy(Coord(9, 15), Coord(13, 11)) == False
