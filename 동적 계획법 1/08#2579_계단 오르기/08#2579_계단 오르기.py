n = int(input())
dp=[]

for m in range(n):
    dp.append(int(input()))

res =[0]*(n+1)
res[1]=dp[0]

if n>=2:
    res[2]=dp[0]+dp[1]
    for i in range(2,n):
        res[i+1]+=max(dp[i-1]+res[i-2],res[i-1])+dp[i]

print(res[n])