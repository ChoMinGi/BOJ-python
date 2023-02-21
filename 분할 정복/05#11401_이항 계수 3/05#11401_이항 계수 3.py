n,k= map(int, input().split())
p= 1000000007

def factorial(N):
    n=1
    for i in range(2,N+1):
        n=(n*i)%p
    return n

def expdiv(n,e):
    if e==0:
        return 1
    elif e==1:
        return n
    else:
        td=expdiv(n,e//2)
        if e%2:
            return td*td*n%p
        else:
            return td*td%p
    
top = factorial(n)%p
bottom = expdiv(factorial(n-k)*factorial(k)%p,p-2)

print(top*bottom%p)

