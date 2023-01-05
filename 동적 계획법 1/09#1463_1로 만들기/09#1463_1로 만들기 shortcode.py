n = int(input())
dp =[0]*(n+1)

dp[0]=-1
dp[1]=0

for i in range(2,n+1):
    dp[i]=min(dp[i-1], dp[i//2]+i%2, dp[i//3]+i%3)+1

print(dp[-1])
