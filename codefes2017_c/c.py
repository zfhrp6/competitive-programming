from collections import deque


def insert_c(s, idx, c):
    return s[:idx] + c + s[idx:]


def calc(s):
    if s == s[::-1]:
        return 0
    if s.replace('x', '') != s.replace('x', '')[::-1]:
        return -1
    # import ipdb;ipdb.set_trace()
    revs = deque(s[::-1])
    s = deque(s)
    cnt = 0
    o_gap, r_gap = 0, 0
    idx = 0
    while idx + o_gap <= len(s) / 2 and idx + r_gap <= len(s) / 2:
        print(cnt, o_gap, r_gap, idx)
        print(' ' + ''.join(s) + '\n', ''.join(revs))
        print(' ' + ' ' * idx + '^')
        if s[idx + o_gap] != revs[idx + r_gap]:
            # print(s[idx + o_gap], revs[idx + r_gap])
            if s[idx + o_gap] == 'x':
                revs.insert(idx, 'x')  # = insert_c(revs, idx, 'x')
                s.insert(len(s) - idx, 'x')
                # r_gap -= 1
            elif revs[idx + r_gap] == 'x':
                s.insert(idx, 'x')  # = insert_c(s, idx, 'x')
                revs.insert(len(revs) - idx, 'x')
                # o_gap -= 1
            cnt += 1
        else:
            idx += 1
    return cnt


def main():
    s = input()
    print(calc(s))


if __name__ == '__main__':
    main()
