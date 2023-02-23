import sys
input = sys.stdin.readline


def matrixexp(a,b): 
    res=[[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n): 
            td=0
            for l in range(n):
                td+=a[i][l]*b[l][j]
            res[i][j]=td%1000
    return res

def conquer(res,k):
    if k==1:
        for i in range(n):
            for j in range(n):
                res[i][j]=res[i][j]%1000
        return res
    else:
        tplist=[]
        tplist= conquer(res,k//2)
        if k%2:
            return matrixexp(matrixexp(tplist,tplist),res)
        else:
            return matrixexp(tplist,tplist)


a=[]
n,k = map(int, input().split())
for _ in range(n):
   a.append(list(map(int, input().split())))

lists=conquer(a,k)
for list in lists:
    print(*list)