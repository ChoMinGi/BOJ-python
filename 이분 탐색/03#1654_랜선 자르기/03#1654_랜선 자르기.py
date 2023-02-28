n,k = map(int,input().split())
lan=[]
for i in range(n):
    lan.append(int(input()))

def lan_possible(n):
    res=0
    for i in lan:
        res+=i//n
    if res>=k:
        return 1
    else:
        return 0
    
def binary_search(ck):
    s=0
    e=ck
    while s<=e:
        mid=(s+e)//2
        if lan_possible(mid):
            ans =mid
            s=mid
        else:
            e=mid
    return ans
print(binary_search(max(lan)))