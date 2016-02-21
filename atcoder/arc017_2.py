import sys
def main():
    n,k = map(int, sys.stdin.readline().split(" "))
    answer = 0
    inc = 1
    prev = int(sys.stdin.readline())
    for i in range(n-1):
        now = int(sys.stdin.readline())
        if now>prev:
            inc += 1
        else:
            if inc>(k-1):
                answer += inc-(k-1)
            inc = 1
        prev = now
    if inc>(k-1):
        answer += inc-(k-1)
    print(answer)

if __name__ == '__main__':
    main()
