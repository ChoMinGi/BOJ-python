import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())

ab=[]
for _ in range(2*n):
    ab.append(list(map(int,input().split())))

for i in range(n):
    res=[]
    for j in range(m):
        res.append(ab[i][j]+ab[i+n][j])
    print(*res)