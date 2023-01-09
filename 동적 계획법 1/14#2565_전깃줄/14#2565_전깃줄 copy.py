n=int(input())
a=sorted([[*map(int,input().split())]for _ in range(n)])
dp=[0]*501
for i,j in a:dp[j]=max(dp[:j])+1
print(n-max(dp))