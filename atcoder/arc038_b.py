# coding: utf-8


def det(y,x,mat,mem):
    if y>=len(mat) or x >= len(mat[0]):
        return 'w'
    if mat[y][x] == '#':
        return 'w'
    if mem[y][x] != '.':
        return mem[y][x]
    result = 'l'
    if det(y,x+1,mat,mem) == 'l':
        result = 'w'
    if det(y+1,x,mat,mem) == 'l':
        result = 'w'
    if det(y+1,x+1,mat,mem) == 'l':
        result = 'w'
    mem[y][x] = result
    return result


def main():
    nrows, ncols = [i for i in map(int, input().split(' '))]
    matrix = []
    for row in range(nrows):
        matrix.append(input())
    mem = []
    for y in range(nrows):
        mem.append([])
        for x in range(ncols):
            mem[y].append('.')
    # for y in range(nrows-1,-1,-1):
    #     for x in range(ncols-1,-1,-1):
    #         det(y,x,matrix,mem)
    print('Second' if det(0,0,matrix,mem)=='l' else 'First')

if __name__ == '__main__':
    main()
