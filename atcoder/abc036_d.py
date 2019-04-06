n = int(input())
bridges = [tuple(map(int, input().split())) for _ in range(n)]

mod = lambda x: x%10**9+7
