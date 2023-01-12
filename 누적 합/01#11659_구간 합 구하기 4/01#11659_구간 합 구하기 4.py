import sys

input = sys.stdin.readline
n ,m = map(int,input().split())
a = [0]+list(map(int,input().split()))

for l in range(2,n+1):
    a[l]+=a[l-1]
res =[]
for o in range(m):
    i ,j = map(int,input().split())
    res.append(a[j]-a[i-1])

print(*res,sep='\n')
