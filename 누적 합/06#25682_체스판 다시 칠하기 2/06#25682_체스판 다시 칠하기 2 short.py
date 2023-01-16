import sys
input = sys.stdin.readline

n,m,k = list(map(int,input().rstrip().split()))

w=[[0]*(m+1) for j in range(n+1)]

for i in range(1,n+1):
    a= list(input().rstrip())
    for j in range(1,m+1):
        w[i][j]=w[i-1][j]+w[i][j-1]-w[i-1][j-1]
        if ((j+i)%2) ^ (a[j-1]=="B"):
            w[i][j]+=1

ans=[]
for r in range(k,n+1):
    for s in range(k,m+1):
        ans.append(w[r][s]-w[r-k][s]-w[r][s-k]+w[r-k][s-k])
        
print(min(min(ans),k**2-max(ans)))