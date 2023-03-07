import sys

input = sys.stdin.readline

n = int(input())
a=[]
for _ in range(n):
    a.append(list(map(int,input().split())))

res = [[0] * n for _ in range(n)]

for c in range(1, n):
    for r in range(n-c):
            j=r+c
            minimum=[res[r][i]+res[i+1][j]+a[r][0]*a[j][1]*a[i][1] for i in range(r,j)]
            res[r][j]=min(minimum)

print(res[0][n - 1])
