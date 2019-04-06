def output(case_number, ans):
    print('Case #{case_number}: {ans}'.format(case_number=case_number,ans=ans))


def calc_a_case(grid_size, lydia_path):
    return ''.join(['E' if l=='S' else 'S' for l in lydia_path])


def main():
    T = int(input())
    for case_idx in range(1,T+1):
        output(case_idx, calc_a_case(int(input()), input()))


if __name__ == '__main__':
    main()
