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


class Coord(namedtuple('Coord', ['x', 'y'])):
    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y)

    def move(self, vec: SelfCoord) -> SelfCoord:
        return Coord(self.x + vec.x, self.y + vec.y)


Choice = Tuple[Coord, Tuple[Coord, Coord, Coord]]


class Line:
    def __init__(self, s: Coord, e: Coord):
        if s.x == e.x and s.y > e.y:
            s, e = e, s
        if s.x > e.x:
            s, e = e, s
        self._s = s
        self._e = e
        self._tuple = (s, e)

    def __hash__(self):
        return hash(self._tuple)

    def __repr__(self):
        return f'({self._s.x},{self._s.y}),({self._e.x},{self._e.y})'

    def __eq__(self, other):
        return self._s == other.s and self._e == other.e

    @property
    def e(self):
        return self._e

    @property
    def s(self):
        return self._s

    def internal_lattice(self) -> Iterator[Coord]:
        if self.s.x == self.e.x:
            for i in range(1, self.e.y - self.s.y):
                yield Coord(self.s.x, self.s.y + i)
        elif self.s.y == self.e.y:
            for i in range(1, self.e.x - self.s.x):
                yield Coord(self.s.x + i, self.s.y)
        elif self.s.y < self.e.y:
            for i in range(1, self.e.y - self.s.y):
                yield Coord(self.s.x + i, self.s.y + i)
        else:  # s.y > e.y
            for i in range(1, self.s.y - self.e.y):
                yield Coord(self.s.x + i, self.s.y - i)


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
        self._lines = set()

    @property
    def points(self) -> Set[Coord]:
        return self._points

    @cached_property
    def sum_of_weights(self) -> float:
        s = 0
        for x in range(self.size):
            for y in range(self.size):
                s += self.weight(self.size, x, y)
        return s

    @staticmethod
    def weight(size: int, x: int, y: int) -> float:
        c = (size - 1) / 2
        return (x - c) ** 2 + (y - c) ** 2 + 1

    @property
    def score(self) -> int:
        sum_of_w = sum([self.weight(self.size, p.x, p.y) for p in self.points])
        score = ((10 ** 6) * (self.size ** 2) * sum_of_w) / (self._number_of_initial_points * self.sum_of_weights)
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
    def _calc_choice_lines(c: Choice) -> List[Line]:
        np = c[0]
        others = c[1]
        return [
            Line(np, others[0]),
            Line(others[0], others[1]),
            Line(others[1], others[2]),
            Line(others[2], np),
        ]

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
        self._lines.update(self._calc_choice_lines((new_point, existing_3_points)))

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

    @staticmethod
    def is_on_line(p: Coord, line: Line) -> bool:
        return p in line.internal_lattice()

    def is_on_any_line(self, p: Coord) -> bool:
        """
        check p is on any line

        Returns:
            bool: True if p is on any line
        """
        for line in self._lines:
            if self.is_on_line(p, line):
                return True
        return False

    def search_candidate_choices_from_point(self, p: Coord) -> Iterator[Tuple[Coord, List[Coord]]]:
        def is_valid_choice(c: Choice) -> bool:
            lines = self._calc_choice_lines(c)
            if set(lines) & self._lines:
                return False
            choice_lattice = []
            for line in lines:
                choice_lattice.extend(line.internal_lattice())
            for p_ in self.points:
                if p_ in choice_lattice:
                    return False
            return (
                    0 <= c[0].y < self.size
                    and 0 <= c[0].x < self.size
                    and c[0] not in self.points
                    and self.is_vacancy(c[0], c[1][0])
                    and self.is_vacancy(c[0], c[1][2])
                    and not self.is_on_any_line(c[0])
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
    # board.choose((9, 15), [(12, 12), (15, 15), (12, 18)])
    while True:
        num_of_can = 10
        candidates = list(islice(board.search_candidate_choices(), num_of_can))
        num_of_can = len(candidates)
        if time() - start_time > 4.5:
            break
        if num_of_can == 0:
            break
        bs = [board.copy() for _ in range(num_of_can)]
        for ci in range(num_of_can):
            bs[ci].choose(*candidates[ci])
        board = sorted(bs, key=lambda b: b.score, reverse=True)[0]
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
