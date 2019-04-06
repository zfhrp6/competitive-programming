from read import read
from Euler import primecheck


def inc_bin(num):
    return bin(int(num, 2) + int('10', 2))[2:]


def first_divisor(num, start=3):
    if num>2 and num%2 == 0:
        return 2
    i = start
    while i**2 <= num:
        if num%i == 0:
            return i
        i+=2
    return False


def calc(dig, start):
    ret = [start]
    s = start
    while True:
        for i in range(2, 11):
            # print(i, end='')
            # print(ret)
            tmp = first_divisor(int(s, i))
            if tmp:
                ret.append(tmp)
                continue
        if len(ret) == 10:
            # print(ret)
            return ret, s
        s = inc_bin(s)
        ret = [s]


def main():
    import sys
    infile = read(sys.argv[1])
    outfilename = sys.argv[2]
    def it():
        return next(infile)

    T = int(it())

    with open(outfilename, 'w') as outfile:
        num_of_digits, num_of_case = map(int, it().split())
        outfile.write('Case #1:\n')
        print('Case #1:')
        current_val = '1'+'0'*(num_of_digits-2)+'1'
        for caseidx in range(1, num_of_case+1):
            # num_of_digits, num_of_case = map(int, it().split())
            ans, current_val = calc(num_of_digits, start=current_val)
            current_val = inc_bin(current_val)
            # outfile.write('Case #1:\n')
            # print('Case #1:')
            outfile.write('{}\n'.format(' '.join(map(str, ans))))
            print('{}'.format(' '.join(map(str, ans))))


if __name__ == '__main__':
    main()
