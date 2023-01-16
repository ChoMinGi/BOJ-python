import sys
input = sys.stdin.readline

n,m = map(int, input().rstrip().split())
cs=[[0]*(n+1) for r in range(n+1)]
for i in range(1,n+1):
    td = 1
    for j in map(int, input().rstrip().split()):
        cs[i][td]=cs[i][td-1]+cs[i-1][td]-cs[i-1][td-1]+j
        td+=1
res=0
for k in range(m):
    xf,yf,xe,ye=map(int,input().rstrip().split())
    res=cs[xe][ye]-cs[xe][yf-1]-cs[xf-1][ye]+cs[xf-1][yf-1]
    print(res)