#!/usr/bin/env python3
# coding: utf-8

from collections import namedtuple
from sys import stderr
from typing import List, Tuple, Set, Literal

X = 'x'
Empty = '.'


class Coord(namedtuple('Coord', ['x', 'y'])):
    def __repr__(self):
        return f'({self.x}, {self.y})'


class Board:
    def __init__(self, n: int, points: List[Coord | Tuple[int, int]]):
        self.size = n
        self._field = [[Empty for _ in range(n)] for _ in range(n)]
        for p in points:
            if not isinstance(p, Coord):
                p = Coord(*p)
            self._field[p.y][p.x] = X
        self._points = {p for p in points}
        self._choices: List[Tuple[Coord, List[Coord | Tuple[int, int]]]] = []

    @property
    def points(self) -> Set[Coord]:
        return self._points

    def get_line_points(self, p: Coord | Tuple[int, int], mode: Literal['x', 'y', 'up', 'down', 'all']) -> List[Coord]:
        """
        get points on the same line from p. 

        Args:
            p: point from
            mode: 'x' | 'y' | 'up' | 'down' | 'all'
        """
        mode_set = {'x', 'y', 'up', 'down', 'all'}
        points = []
        if not isinstance(p, Coord):
            p = Coord(*p)
        if mode not in mode_set:
            raise ValueError(f"mode must be {' or '.join(mode_set)}")
        for i in range(self.size):
            if mode == 'x' or mode == 'all':
                x, y = i, p.y
                if self._field[y][x] == X:
                    points.append(Coord(x, y))
            if mode == 'y' or mode == 'all':
                x, y = p.x, i
                if self._field[y][x] == X:
                    points.append(Coord(x, y))
            if mode == 'up' or mode == 'all':  # positive gradient
                x, y = i, (p.y - p.x + i)
                if y < 0 or y >= self.size or x < 0 or x >= self.size:
                    continue
                if self._field[y][x] == X:
                    points.append(Coord(x, y))
            if mode == 'down' or mode == 'all':  # negative gradient
                x, y = i, (p.y + p.x - i)
                if y < 0 or y >= self.size or x < 0 or x >= self.size:
                    continue
                if self._field[y][x] == X:
                    points.append(Coord(x, y))
        ret = list(set(points))
        if p in ret:
            ret.remove(p)
        return ret

    def choose(self, new_point: Coord | Tuple[int, int], existing_3_points: List[Coord | Tuple[int, int]]):
        if not isinstance(new_point, Coord):
            new_point = Coord(*new_point)
        if not isinstance(existing_3_points[0], Coord):
            existing_3_points = [Coord(*p) for p in existing_3_points]
        if len(existing_3_points) != 3:
            raise ValueError('3 existing points required')
        if new_point in self._points:
            raise ValueError('new point is already in points')
        self._choices.append((new_point, existing_3_points))
        self._field[new_point.y][new_point.x] = X
        self._points.add(new_point)

    @property
    def choices_count(self) -> int:
        return len(self._choices)

    @property
    def choices(self) -> List[Tuple[Coord, List[Coord]]]:
        return self._choices

    def debug(self, field=True, choices=True, points=True):
        print('debug', file=stderr)

        if field:
            print('field', file=stderr)
            for row in reversed(self._field):
                print(' '.join(row), file=stderr)

        if choices:
            print(f'choices count: {self.choices_count}', file=stderr)
            for c in self._choices:
                np = c[0]
                print(f'{np.x} {np.y} ' + ' '.join([f'{p.x} {p.y}' for p in c[1]]))

        if points:
            print('points', file=stderr)
            for p in self._points:
                print(p)


def solve(board: Board):
    # board.debug(points=False)
    board.choose((9, 15), [(12, 12), (15, 15), (12, 18)])
    board.debug(points=False)
    print(board.get_line_points((9, 15), mode='x'))
    print(board.get_line_points((9, 15), mode='y'))
    print(board.get_line_points((9, 15), mode='up'))
    print(board.get_line_points((9, 15), mode='down'))
    print(board.get_line_points((9, 15), mode='all'))
    pass


def read_input() -> Board:
    n, m = list(map(int, input().split()))
    initial_points = []
    for _ in range(m):
        px, py = list(map(int, input().split()))
        initial_points.append(Coord(px, py))
    return Board(n, initial_points)


def output(board: Board):
    print('output', file=stderr)
    print(board.choices_count)
    for c in board.choices:
        new_p = c[0]
        others = c[1]
        others_str = ' '.join([f'{p.x} {p.y}' for p in others])
        print(f'{new_p.x} {new_p.y} {others_str}')


def main():
    board = read_input()
    solve(board)
    output(board)


if __name__ == '__main__':
    main()
