import sys

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    AB = list(zip(A, B))
    bigger_diff = list(map(lambda ab: max(ab[0] - ab[1], 0), AB))
    lesser_diff = list(map(lambda ab: min(ab[0] - ab[1], 0), AB))
    exceeded = sum(bigger_diff)
    shortage = sum(lesser_diff)

    if exceeded < abs(shortage):
        print(-1)
        sys.exit()

    if all(map(lambda ab: ab[0] >= ab[1], AB)):
        print(0)
        sys.exit()



    ans = len(list(filter(lambda d: d<0, lesser_diff)))

    bigger_diff = sorted(bigger_diff, reverse=True)

    ss = 0
    for i in range(len(bigger_diff)):
        ss += bigger_diff[i]
        if ss >= abs(shortage):
            ans += i + 1
            break
    print(ans)



if __name__=='__main__':
    main()
