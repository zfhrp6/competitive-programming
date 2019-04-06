N = int(input())


def f(N):
    if N % 2:
        d, step = 4, 4
    else:
        print(N // 2, N, N)
        return 0
    for h in range(d, 3501, 4):
        for n in range(d, h + 1, 4):
            for w in range(1, n + 1, 1):
                # if 4 * h * n * w > N * (n*w + h*w + h*n):
                #     continue
                if not w % 300:
                    print(h,n,w, 4 * h * n * w,N*(n*w+h*w+h*n))
                if 4 * h * n * w == N * (n*w + h*w + h*n):
                    print(h, n, w)
                    return 0


f(N)
