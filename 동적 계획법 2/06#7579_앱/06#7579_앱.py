import sys

input = sys.stdin.readline

n, m = map(int, input().split())
mmlist = list(map(int, input().split()))
cost = list(map(int, input().split()))
w = sum(cost)
dp = [[0] * (w + 1) for _ in range(n + 1)]
res = w

for i in range(1, n + 1):
    tm = mmlist[i - 1]
    tc = cost[i - 1]
    for j in range(1, w + 1):
        dp[i][j] = dp[i - 1][j]
    for k in range(tc, w + 1):
        dp[i][k] = max(dp[i - 1][k - tc] + tm, dp[i][k])
        if dp[i][k] >= m:
            res = min(res, k)
print(res)
