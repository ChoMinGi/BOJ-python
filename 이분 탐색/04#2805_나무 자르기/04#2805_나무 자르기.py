import sys
input = sys.stdin.readline

n,m = map(int,input().split())
tree = list(map(int,input().split()))

def cut_left(cut):
    res=0
    for i in tree:
        td=i-cut
        if td>0:
            res+=td
    if res>=m:
        return 1
    else:
        return 0
    
def binary_search(h):
    s=0
    e=h
    while s<=e:
        mid=(s+e)//2
        
        if cut_left(mid):
            ans=mid
            s=mid+1
        else:
            e=mid-1
    return ans
print(binary_search(max(tree)))
