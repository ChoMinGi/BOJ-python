import sys
n = int(input())
dp=[]
for m in range(n):
    dp.append([0]+list(map(int,input().split()))+[0])
for i in range(1,n):
    for j in range(1,i+2):
        dp[i][j] = max(dp[i-1][j-1],dp[i-1][j])+dp[i][j]
print(max(dp[n-1]))
print(dp)
