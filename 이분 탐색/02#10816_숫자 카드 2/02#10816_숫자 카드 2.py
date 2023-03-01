import sys
input =sys.stdin.readline

n = int(input())
alist = list(map(int, input().split()))
alist.sort()
m = int(input())
sglist=(list(map(int,input().split())))


def binary_search(tg):
    s=0
    e=len(alist)-1
    while s<=e:
        mid = (s+e)//2
        td=0
        if alist[mid]>=tg:
            ans = mid
            e=mid-1
    