n,k= map(int, input().split())
p= 1000000007

def factorial(N):
    n=1
    for i in range(2,N+1):
        n*=i%p
    return n

def expdiv(n,e):
    if e==0:
        return 1
    elif e==1:
        return n
    else:
        if e%2:
            return expdiv(n,e//2)*n%p
        else:
            return expdiv(n,e//2)%p
    
top = factorial(n)
bottom = expdiv(factorial(n-k)*factorial(k),p-2)

print(top*bottom%p)

