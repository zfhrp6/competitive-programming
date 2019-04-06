def print_answer(case_number, n):
    print('Case #{}: {}'.format(case_number, n))


def calc_damage(s):
    strength = 1
    damage = 0
    for c in s:
        if c == 'C':
            strength *= 2
        else:
            damage += strength
    return damage


def one_swap(s):
    if 'C' not in s:
        return s
    if 'S' not in s:
        return s
    last_shoot = s.rfind('S')
    last_charge_before_shoot = s[:last_shoot].rfind('C')
    if last_charge_before_shoot == -1:
        return s
    return s[:last_charge_before_shoot] + 'S' + 'C' + s[last_charge_before_shoot + 2:]


def main():
    T = int(input())
    for tidx in range(1, T + 1):
        shield, proc = list(input().split())
        shield = int(shield)
        cnt = 0
        while proc != one_swap(proc) and calc_damage(proc) > shield:
            proc = one_swap(proc)
            cnt += 1
        if calc_damage(proc) > shield:
            print_answer(tidx, 'IMPOSSIBLE')
        else:
            print_answer(tidx, cnt)

    pass


if __name__ == '__main__':
    main()
