#!/usr/bin/env python3
# coding: utf-8

import random
from collections import namedtuple
from functools import cached_property
from sys import stderr
from typing import Iterator, List, Tuple, Set, Literal, TypeVar, Union

random.seed(2)

X = 'x'
Empty = '.'

SelfCoord = TypeVar('SelfCoord', bound='Coord')
SelfBoard = TypeVar('SelfBoard', bound='Board')
SelfLine = TypeVar('SelfLine', bound='LIne')


class Coord(namedtuple('Coord', ['x', 'y'])):
    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y)

    def move(self, vec: SelfCoord) -> SelfCoord:
        return Coord(self.x + vec.x, self.y + vec.y)


Choice = Tuple[Coord, Tuple[Coord, Coord, Coord]]


class Line:
    """
    1-unit line
    """

    def __init__(self, s: Coord, e: Coord):
        if s.y > e.y:
            s, e = e, s
        if s.x > e.x:
            s, e = e, s
        self._s = s
        self._e = e
        self._tuple = (s, e)

    def __hash__(self):
        return hash(self._tuple)

    def __repr__(self):
        return f'({self._s.x},{self._s.y})-({self._e.x},{self._e.y})'

    def __eq__(self, other):
        return self._s == other.s and self._e == other.e

    @classmethod
    def new(cls, s: Coord, e: Coord) -> Iterator[SelfLine]:
        if abs(e.x - s.x) < 2 and abs(e.y - s.y) < 2:
            return [Line(s, e)]
        return cls._split_line(s, e)

    @classmethod
    def _split_line(cls, s: Coord, e: Coord) -> Iterator[SelfLine]:
        if s.y > e.y:
            s, e = e, s
        if s.x > e.x:
            s, e = e, s
        # s must be left than(or equal) e, s may be left than (or equal) e.

        if s.x == e.x:
            for i in range(0, abs(e.y - s.y)):
                yield Line(Coord(s.x, s.y + i),
                           Coord(s.x, s.y + (i + 1)))
        elif s.y == e.y:
            for i in range(0, abs(e.x - s.x)):
                yield Line(Coord(s.x + i, s.y),
                           Coord(s.x + (i + 1), s.y))
        else:
            sgn = 1 if e.y > s.y else -1
            for i in range(0, abs(e.y - s.y)):
                yield Line(Coord(s.x + i, s.y + sgn * i),
                           Coord(s.x + (i + 1), s.y + sgn * (i + 1)))

    @property
    def e(self):
        return self._e

    @property
    def s(self):
        return self._s


class Board:
    def __init__(self, n: int, points: List[Coord]):
        self.size = n
        self._field = [[Empty for _ in range(n)] for _ in range(n)]
        for p in points:
            self._field[p.y][p.x] = X
        self._initial_points = points
        self._number_of_initial_points = len(points)
        self._points = {p for p in points}
        self._choices: List[Choice] = []
        self._lines: Set[Line] = set()

    @cached_property
    def board_weight(self) -> float:
        n = self.size
        c = (n - 1) / 2
        return (
                n ** 2
                + 2 * (n ** 2) * ((c + 1) ** 2)
                - 2 * (c + 1) * (n ** 2) * (n + 1)
                + (1 / 3) * (n ** 2) * (n + 1) * (2 * n + 1)
        )

    @property
    def points(self) -> Set[Coord]:
        return self._points

    @staticmethod
    def weight(size: int, x: int, y: int) -> float:
        c = (size - 1) / 2
        return (x - c) ** 2 + (y - c) ** 2 + 1

    @property
    def score(self) -> int:
        sum_of_w = sum([self.weight(self.size, p.x, p.y) for p in self.points])
        score = ((10 ** 6) * (self.size ** 2) * sum_of_w) / (self._number_of_initial_points * self.board_weight)
        return round(score)

    def _out_of_range(self, x, y):
        return x < 0 or x >= self.size or y < 0 or y >= self.size

    def get_line_points(
            self,
            p: Union[Coord, Tuple[int, int]],
            mode: Literal['x', 'y', 'up', 'down', 'all']
    ) -> List[Coord]:
        """
        get points on the same line from p. 

        Args:
            p: point from
            mode: search mode
        """
        mode_set = {'x', 'y', 'up', 'down', 'all'}
        points = []
        if not isinstance(p, Coord):
            p = Coord(*p)
        if mode not in mode_set:
            raise ValueError(f"mode must be {' or '.join(mode_set)}")

        if mode == 'x' or mode == 'all':
            for i in range(1, self.size - 1):
                x, y = p.x + i, p.y
                if self._out_of_range(x, y):
                    break
                if self._field[y][x] == X:
                    points.append(Coord(x, y))
                    break

            for i in range(1, self.size - 1):
                x, y = p.x - i, p.y
                if self._out_of_range(x, y):
                    break
                if self._field[y][x] == X:
                    points.append(Coord(x, y))
                    break

        if mode == 'y' or mode == 'all':
            for i in range(1, self.size - 1):
                x, y = p.x, p.y + i
                if self._out_of_range(x, y):
                    break
                if self._field[y][x] == X:
                    points.append(Coord(x, y))
                    break
            for i in range(1, self.size - 1):
                x, y = p.x, p.y - i
                if self._out_of_range(x, y):
                    break
                if self._field[y][x] == X:
                    points.append(Coord(x, y))
                    break

        if mode == 'up' or mode == 'all':  # positive gradient
            for i in range(1, self.size - 1):
                x, y = p.x + i, p.y + i
                if self._out_of_range(x, y):
                    break
                if self._field[y][x] == X:
                    points.append(Coord(x, y))
                    break
            for i in range(1, self.size - 1):
                x, y = p.x - i, p.y - i
                if self._out_of_range(x, y):
                    break
                if self._field[y][x] == X:
                    points.append(Coord(x, y))
                    break

        if mode == 'down' or mode == 'all':  # negative gradient
            for i in range(1, self.size - 1):
                x, y = p.x + i, p.y - i
                if self._out_of_range(x, y):
                    break
                if self._field[y][x] == X:
                    points.append(Coord(x, y))
                    break
            for i in range(1, self.size - 1):
                x, y = p.x - i, p.y + i
                if self._out_of_range(x, y):
                    break
                if self._field[y][x] == X:
                    points.append(Coord(x, y))
                    break

        ret = list(set(points))
        if p in ret:
            ret.remove(p)
        return sorted(ret)

    @staticmethod
    def _calc_choice_lines(c: Choice) -> Iterator[Line]:
        from itertools import chain
        np = c[0]
        others = c[1]
        return chain(
            Line.new(np, others[0]),
            Line.new(others[0], others[1]),
            Line.new(others[1], others[2]),
            Line.new(others[2], np),
        )

    def choose(self, new_point: Coord, existing_3_points: Tuple[Coord, Coord, Coord]):
        if not isinstance(new_point, Coord):
            new_point = Coord(*new_point)
        if not isinstance(existing_3_points[0], Coord):
            existing_3_points = tuple([Coord(*p) for p in existing_3_points])
        if len(existing_3_points) != 3:
            raise ValueError('3 existing points required')
        if new_point in self._points:
            raise ValueError('new point is already in points')
        self._choices.append((new_point, existing_3_points))
        self._field[new_point.y][new_point.x] = X
        self._points.add(new_point)
        new_lines = self._calc_choice_lines((new_point, existing_3_points))
        self._lines.update(new_lines)

    def is_vacancy(self, s: Coord, e: Coord) -> bool:
        """
        can draw line between s and e

        Returns:
            bool: True if you can draw line between s and e
        """
        if s == e:
            return False
        if s.x == e.x:
            if s.y < e.y:
                for i in range(1, e.y - s.y):
                    if self._field[s.y + i][s.x] == X:
                        return False
                return True
            else:
                for i in range(1, s.y - e.y):
                    if self._field[s.y - i][s.x] == X:
                        return False
                return True
        if s.y == e.y:
            if s.x < e.x:
                for i in range(1, e.x - s.x):
                    if self._field[s.y][s.x + i] == X:
                        return False
                return True
            else:
                for i in range(1, s.x - e.x):
                    if self._field[s.y][s.x - i] == X:
                        return False
                return True
        if s.y < e.y:
            if s.x < e.x:
                for i in range(1, e.y - s.y):
                    if self._field[s.y + i][s.x + i] == X:
                        return False
                return True
            else:
                for i in range(1, e.y - s.y):
                    if self._field[s.y + i][s.x - i] == X:
                        return False
                return True
        else:  # s.y > e.y
            if s.x < e.x:
                for i in range(1, s.y - e.y):
                    if self._field[s.y - i][s.x + i] == X:
                        return False
                return True
            else:
                for i in range(1, s.y - e.y):
                    if self._field[s.y - i][s.x - i] == X:
                        return False
                return True

    def is_overlapped(self, c: Choice) -> bool:
        lines = self._calc_choice_lines(c)
        for line in lines:
            if line in self._lines:
                return True
        return False

    def search_candidate_choices_from_point(self, p: Coord) -> Iterator[Tuple[Coord, List[Coord]]]:
        def is_valid_choice(c: Choice) -> bool:
            return (
                    0 <= c[0].y < self.size
                    and 0 <= c[0].x < self.size
                    and c[0] not in self.points
                    and self.is_vacancy(c[0], c[1][0])
                    and self.is_vacancy(c[0], c[1][2])
                    and not self.is_overlapped(c)
            )

        if p not in self.points:
            return None
        p0 = p

        p1s = self.get_line_points(p0, mode='x')
        for p1 in p1s:
            p2s = self.get_line_points(p1, mode='y')
            for p2 in p2s:
                p3 = Coord(p0.x, p2.y)
                if is_valid_choice((p3, (p0, p1, p2))):
                    yield p3, (p0, p1, p2)

        p1s = self.get_line_points(p0, mode='y')
        for p1 in p1s:
            p2s = self.get_line_points(p1, mode='x')
            for p2 in p2s:
                p3 = Coord(p2.x, p0.y)
                if is_valid_choice((p3, (p0, p1, p2))):
                    yield p3, (p0, p1, p2)

        p1s = self.get_line_points(p0, mode='up')
        for p1 in p1s:
            p2s = self.get_line_points(p1, mode='down')
            for p2 in p2s:
                vec = p2 - p1
                p3 = p0.move(vec)
                if is_valid_choice((p3, (p0, p1, p2))):
                    yield p3, (p0, p1, p2)

        p1s = self.get_line_points(p0, mode='down')
        for p1 in p1s:
            p2s = self.get_line_points(p1, mode='up')
            for p2 in p2s:
                vec = p2 - p1
                p3 = p0.move(vec)
                if is_valid_choice((p3, (p0, p1, p2))):
                    yield p3, (p0, p1, p2)

    def search_candidate_choices(self) -> Iterator[Tuple[Coord, List[Coord]]]:
        for p0 in self.points:
            for candidate in self.search_candidate_choices_from_point(p0):
                yield candidate

    @property
    def choices_count(self) -> int:
        return len(self._choices)

    @property
    def choices(self) -> List[Tuple[Coord, Tuple[Coord, Coord, Coord]]]:
        return self._choices

    def copy(self) -> SelfBoard:
        b = Board(self.size, self._initial_points)
        b._field = [[self._field[y][x] for x in range(self.size)] for y in range(self.size)]
        b._choices = [choice for choice in self._choices]
        b._lines = {line for line in self._lines}
        b._points = {p for p in self._points}
        return b

    def debug(self, field=True, choices=True, points=True):
        print('debug', file=stderr)

        if field:
            print('field', file=stderr)
            print('  ' + ' '.join([str(i % 10) for i in range(self.size)]), file=stderr)
            for idx, row in enumerate(reversed(self._field)):
                print(str(self.size - idx - 1).zfill(2), end='', file=stderr)
                print(' '.join(row), file=stderr)
            print('  ' + ' '.join([str(i % 10) for i in range(self.size)]), file=stderr)

        if choices:
            print(f'choices count: {self.choices_count}', file=stderr)
            for c in self._choices:
                np = c[0]
                print(f'{np.x} {np.y} ' + ' '.join([f'{p.x} {p.y}' for p in c[1]]))

        if points:
            print('points', file=stderr)
            for p in self._points:
                print(p)


def solve(board: Board) -> Board:
    from time import time
    start_time = time()
    from itertools import islice
    while True:
        num_of_can = 15
        candidates = list(islice(board.search_candidate_choices(), num_of_can))
        num_of_can = len(candidates)
        if time() - start_time > 4.5:
            break
        if num_of_can == 0:
            break
        bs = [board.copy() for _ in range(num_of_can)]
        max_score = 0
        for ci in range(num_of_can):
            b = bs[ci]
            c = candidates[ci]
            b.choose(*c)
            if b.score > max_score:
                board = b
    return board


def read_input() -> Board:
    n, m = list(map(int, input().split()))
    initial_points = []
    for _ in range(m):
        px, py = list(map(int, input().split()))
        initial_points.append(Coord(px, py))
    return Board(n, initial_points)


def output(board: Board):
    # print('output', file=stderr)
    print(board.choices_count)
    for c in board.choices:
        new_p = c[0]
        others = c[1]
        others_str = ' '.join([f'{p.x} {p.y}' for p in others])
        print(f'{new_p.x} {new_p.y} {others_str}')


def main():
    board = read_input()
    board = solve(board)
    output(board)


if __name__ == '__main__':
    main()
