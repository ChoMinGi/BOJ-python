import sys
input = sys.stdin.readline

n, c = map(int,input().split())
c-=1
home=[]

for i in range(n):
    home.append(int(input()))
home.sort()

def select(d):
    t=c
    preH=home[0]
    for i in range(1,len(home)):
        if home[i]-preH>=d:
            t-=1
            preH=home[i]
    if t<=0:
        return 1
    else:
        return 0
    
def binary_search(d):
    s=0
    e=d
    while s<=e:
        mid = (s+e)//2
        if select(mid):
            ans=mid
            s=mid+1
        else:
            e=mid-1

    return ans

print(binary_search(home[-1]))