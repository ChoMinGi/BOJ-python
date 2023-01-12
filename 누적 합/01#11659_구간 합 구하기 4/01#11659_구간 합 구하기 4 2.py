n ,m = map(int,input().split())
a = list(map(int,input().split()))
cumsum=[[0 for i in range(n+1)]for j in range(n+1)]
cumsum[1][:] = [0]+ a

res = []

for l in range(2,n+1):
    cumsum[1][l]+=cumsum[1][l-1]
for i in range(2,n+1):
    for j in range(i,n+1):
        cumsum[i][j]=cumsum[i-1][j]-cumsum[i-1][i-1]

for o in range(m):
    i ,j = map(int,input().split())
    res.append(cumsum[i][j])

print(*res,sep='\n')
