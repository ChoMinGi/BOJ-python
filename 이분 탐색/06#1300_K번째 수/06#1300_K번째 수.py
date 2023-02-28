n= int(input())
k= int(input())


def kcount(tg):
    td=0
    for i in range(1,n+1):
        td+=min(tg//i,n)
    if td>=k:
        return 1
    else:
        return 0

def binary_search(end):
    s=1
    e=end
    ans=0
    while s<=e:
        mid = (s+e)//2

        if kcount(mid):
            ans=mid
            e=mid-1
        else:
            s=mid+1

    return ans
        
print(binary_search(n*n))