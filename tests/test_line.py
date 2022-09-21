from typing import Iterator

from solver import Line, Coord


class TestLine:
    def setup_method(self):
        pass

    @staticmethod
    def _assert_lines(ls1: Iterator[Line], ls2: Iterator[Line]) -> bool:
        if len(list(ls1)) != len(list(ls2)):
            return False
        for line in ls1:
            if line not in ls2:
                return False
        return True

    def test_new_x(self):
        lines = Line.new(Coord(1, 1), Coord(3, 1))
        assert self._assert_lines(lines, [Line(Coord(1, 1), Coord(2, 1)), Line(Coord(2, 1), Coord(3, 1))]), lines

    def test_new_y(self):
        lines = Line.new(Coord(1, 1), Coord(1, 3))
        assert self._assert_lines(lines, [Line(Coord(1, 1), Coord(1, 2)), Line(Coord(1, 2), Coord(1, 3))]), lines

    def test_new_up(self):
        lines = Line.new(Coord(1, 1), Coord(3, 3))
        assert self._assert_lines(lines, [Line(Coord(1, 1), Coord(2, 2)), Line(Coord(2, 2), Coord(3, 3))]), lines

    def test_new_down(self):
        lines = Line.new(Coord(1, 3), Coord(3, 1))
        assert self._assert_lines(lines, [Line(Coord(1, 3), Coord(2, 2)), Line(Coord(2, 2), Coord(3, 1))]), lines

    def test_new_reversed(self):
        lines = Line.new(Coord(3, 1), Coord(1, 3))
        assert self._assert_lines(lines, [Line(Coord(1, 3), Coord(2, 2)), Line(Coord(2, 2), Coord(3, 1))]), lines
