def factoring(n):
    for i in range(100, 0, -1):
        if n%i == 0:
            return i
    return n

def is_sq(n):
    for i in range(1,100):
        if i**2 == n:
            return True
    return False

def make_ichimatsu(n):
    height = factoring(n)
    width = n // height
    if width%2:
        width, height = height, width
    ret = []
    for h in range(height):
        line = '#.' * (width//2)
        line = line[h%2:] + line[:h%2]
        ret.append(line)
    return (height, width, ret)

def make_oddichimatsu(w,b):
    width = height = factoring(w+b)
    ret = '.' * (w>b) + '#.' * (n-1) + '#' * (w<b)
    ret = list(map(''.join, zip(*[iter(ret)]*height)))
    return (height, width, ret)



def calc(W, B):
    if W==B and factoring(W+B)<W+B:
        return make_ichimatsu(W+B)

def main():
    W, B = list(map(int, input().split()))

    # 初期マップ生成（上半分が城，下半分が黒の100x100）
    ret = '.'*100*50 + '#'*100*50
    ret = list(map(list, zip(*[iter(ret)]*100)))

    # 白の世界に黒ドットを(指定-1)個数だけ打ち込む（2列2行ごとに1点）
    for bidx in range(B-1):
        ret[(bidx//50)*2][(bidx%50)*2] = '#'
    
    # 黒の世界に城ドットを(指定-1)個数だけ打ち込む（2列2行ごとに1点）
    for widx in range(W-1):
        ret[99-(widx//50)*2][99-(widx%50)*2] = '.'

    print('{} {}'.format(100, 100))
    for line in ret:
        print(''.join(line))

if __name__ == '__main__':
    main()
