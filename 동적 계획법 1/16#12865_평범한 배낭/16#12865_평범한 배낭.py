n, k = map(int,input().split())
pd = [[0 for i in range(k+1)] for j in range(n+1)]

for i in range(1,n+1):
    w, v = map(int,input().split())
    for j in range(1,k+1):
        if j<w:
            pd[i][j] = pd[i-1][j]
        else:
            pd[i][j] = max(v + pd[i-1][j-w], pd[i-1][j])

print(max(map(max,pd)))