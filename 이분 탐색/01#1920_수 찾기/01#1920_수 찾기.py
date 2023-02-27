import sys
input = sys.stdin.readline

input()
a = list(map(int,input().split()))
a.sort()

def binary_search(ck,a):
    s=0
    e=len(a)-1

    while s<=e:
        mid=(s+e)//2
        if a[mid]==ck:
            return 1
        elif a[mid]<ck:
            s=mid+1
        else:
            e=mid-1
    
    return 0

input()

for i in list(map(int,input().split())):
    if binary_search(i,a):
        print("1")
    else:
        print("0")