n=int(input())

a=[[1,1],[1,0]]
def fibo(n):
    if n==0 or n==1:
        return a
    else:
        tl=fibo(n//2)
        if n%2:
            return matricexp(matricexp(tl,tl),a)
        else:
            return matricexp(tl,tl)

def matricexp(a,b):
    res=[[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            td=0
            for l in range(2):
                td+= a[i][l]*b[l][j]%1000000007
            res[i][j]=td%1000000007
    return res

print(fibo(n-1)[0][0])