import sys

input = sys.stdin.readline

n, m = map(int, input().split())
mmlist = list(map(int, input().split()))
cost = list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    tm = mmlist[i - 1]
    tc = cost[i - 1]
    dp[i][tm] += tc
    for j in range(1, m + 1):
        ptd = dp[i - 1][j]
        if ptd != 0:
            dp[i][j] = ptd
            addData = dp[i][min(j + tm, m)]
            if addData == 0:
                dp[i][min(j + tm, m)] = ptd + tc
            else:
                dp[i][min(j + tm, m)] = min(addData, ptd + tc)

print(dp[-1][-1])
