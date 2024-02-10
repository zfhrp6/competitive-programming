from dataclasses import dataclass, field


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


def answer(ps: list[Coordinate]) -> str:
    set_ = set(ps)
    s = f'a {len(set_)} ' + ' '.join([f'{p[0]} {p[1]}' for p in set_])
    return s
    
def p_answer(ps: list[Coordinate]):
    print(answer(ps))


@dataclass
class Problem:
    N: int
    M: int
    eps: float
    fields: list[Field] = field(default_factory=list)

    def __str__(self):
        ret = f'''N: {self.N}
M: {self.M}
eps: {self.eps}
'''
        for idx, f in enumerate(self.fields):
            ret += f'field[{idx}](size: {f[0]}):\n'
            ret += matrix(self.N, f[1])
            ret += '\n'
        return ret
    
    def add_field(self, field: Field):
        self.fields.append(field)

    def solve(self) -> list[Coordinate]:
        return NotImplemented


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
            ps.append((int(line[2*i+1]), int(line[2*i+2])))
        problem.add_field((d, ps))
    debug_print(problem)
        
    # drill every square
    has_oil = []
    for i in range(N):
        for j in range(N):
            p_dig((i, j))
            resp = input()
            debug_print(resp)
            if resp != "0":
                has_oil.append((i, j))
        
    p_answer(has_oil)
    resp = input()
    debug_print(resp)
    assert resp == "1", resp

main()