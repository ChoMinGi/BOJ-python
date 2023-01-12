import sys

input = sys.stdin.readline

n ,k = map(int,input().split())
a = list(map(int,input().split()))
res=[0]*(n-k+1)

res[0]=sum(a[0:k])

for l in range(1,n+1-k):
    res[l]=res[l-1]-a[l-1]+a[l+k-1]

print(max(res))
