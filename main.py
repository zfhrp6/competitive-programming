from dataclasses import dataclass, field
from doctest import UnexpectedException


def debug_print(*args, **kwargs):
    import sys

    print(*args, **kwargs, file=sys.stderr)


Coordinate = tuple[int, int]
Field = tuple[int, list[Coordinate]]


def matrix(n: int, mark: None | list[Coordinate] = None) -> str:
    m = ''
    for r in range(n):
        for c in range(n):
            if mark and (c, r) in mark:
                m += '■ '
            else:
                m += '. '
        m += '\n'
    return m


def dig(p: Coordinate) -> str:
    return f'q 1 {p[0]} {p[1]}'


def p_dig(p: Coordinate):
    print(dig(p))


def forecast(ps: list[Coordinate]) -> str:
    set_ = set(ps)
    s = f'q {len(set_)} ' + ' '.join([f'{p[0]} {p[1]}' for p in set_])
    return s


def p_forecast(ps: list[Coordinate]):
    print(forecast(ps))


def answer(ps: set[Coordinate] | list[Coordinate]) -> str:
    set_ = set(ps)
    s = f'a {len(set_)} ' + ' '.join([f'{p[0]} {p[1]}' for p in set_])
    return s


def p_answer(ps: set[Coordinate] | list[Coordinate]):
    print(answer(ps))


@dataclass
class Problem:
    N: int
    M: int
    eps: float
    oil_sum: int = 0
    fields: list[Field] = field(default_factory=list)
    known: set[Coordinate] = field(default_factory=set)
    has_oil: set[Coordinate] = field(default_factory=set)
    found_oil_sum: int = 0
    _next_dig: list[Coordinate] = field(default_factory=list)

    def __str__(self):
        ret = f"""N: {self.N}
M: {self.M}
eps: {self.eps}
oil_sum: {self.oil_sum}
"""
        for idx, f in enumerate(self.fields):
            ret += f'field[{idx}](size: {f[0]}):\n'
            ret += matrix(self.N, f[1])
            ret += '\n'
        return ret

    def add_field(self, field: Field):
        self.fields.append(field)
        self.oil_sum += field[0]

    def found_oil(self, p: Coordinate, value: int):
        self.has_oil.add(p)
        self.found_oil_sum += value

    def solve(self) -> list[Coordinate]:
        return NotImplemented

    def is_solved(self) -> bool:
        return self.found_oil_sum == self.oil_sum or len(self.known) == self.N**2

    def next_dig(self) -> Coordinate:
        return NotImplemented

    def next(self, p: Coordinate) -> Coordinate:
        if self._next_dig:
            while self._next_dig:
                candidate = self._next_dig.pop()
                if candidate not in self.known:
                    return candidate
        nx, ny = p[0] + 1, p[1]
        if ny >= self.N and nx >= self.N:
            return (0, 0)
        if nx >= self.N:
            nx = 0
            ny += 1
        if (nx, ny) not in self.known:
            return (nx, ny)
        return self.next((nx, ny))
    
    def add_next(self, p: Coordinate):
        if 0 <= p[0] < self.N and 0 <= p[1] < self.N:
            self._next_dig.append(p)


def main():
    # read prior information
    line = input().split()
    N = int(line[0])
    M = int(line[1])
    eps = float(line[2])
    problem = Problem(N, M, eps)
    for _ in range(M):
        line = input().split()
        ps = []
        d = int(line[0])
        for i in range(d):
            ps.append((int(line[2 * i + 1]), int(line[2 * i + 2])))
        problem.add_field((d, ps))
    debug_print(problem)

    (i, j) = (0, 0)
    while not problem.is_solved():
        p_dig((i, j))
        problem.known.add((i, j))
        resp = input()
        if resp != '0':
            problem.found_oil((i, j), int(resp))
            # next neighbor
            problem.add_next((i - 1, j))  # left
            problem.add_next((i, j - 1))  # up
            problem.add_next((i + 1, j))  # right
            problem.add_next((i, j + 1))  # down

        (i, j) = problem.next((i, j))

    p_answer(problem.has_oil)
    resp = input()
    assert resp == '1', resp


main()
