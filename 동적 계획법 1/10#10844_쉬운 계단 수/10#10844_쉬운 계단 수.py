n= int(input())
pd=[[0 for i in range(12)] for j in range(n)]
pd[0]=[0,0,1,1,1,1,1,1,1,1,1,0]

if n>=1:
    for i in range(1,n):
        for j in range(1,11):
            pd[i][j] = int(pd[i-1][j-1])+int(pd[i-1][j+1])

print(sum(pd[n-1])%1000000000)
