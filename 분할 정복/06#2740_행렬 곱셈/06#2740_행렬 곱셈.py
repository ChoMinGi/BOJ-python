import sys
input = sys.stdin.readline

a=[]
b=[]

n,m = map(int, input().split())
for _ in range(n):
   a.append(list(map(int, input().split())))

m,k = map(int, input().split())
for _ in range(m):
   b.append(list(map(int, input().split())))

res=[[0 for _ in range(k)]for _ in range(n)]

td=0
for i in range(n):
    for j in range(k):
        for l in range(m):
            td+=a[i][l]*b[l][j]
        print(td,end=' ')
        td=0
    print()

