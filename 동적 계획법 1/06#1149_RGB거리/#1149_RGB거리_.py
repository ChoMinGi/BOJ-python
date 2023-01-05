import sys
n = int(input())
dp=[]
for m in range(n):
    dp.append(list(map(int,input().split())))
for i in range(n-1):
    dp[i+1][0] = min(dp[i][1],dp[i][2])+dp[i+1][0]
    dp[i+1][1] = min(dp[i][0],dp[i][2])+dp[i+1][1]
    dp[i+1][2] = min(dp[i][0],dp[i][1])+dp[i+1][2]

print(min(dp[i+1][0],dp[i+1][1],dp[i+1][2]))