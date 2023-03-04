import sys
from heapq import heapify
input = sys.stdin.readline

def filecombine(list):
    if len(list)<=2:
        return sum(list)
    elif len(list)//2:
        heapify(list)
        return filecombine(list[:-1])+list[-1]
    else:
        td=len(list)//2
        if td//2:
            return filecombine(list[:td-1])+filecombine(list[td-1:])
    




T=int(input())
for i in range(T):
    K=int(input())
    size=list(map(int,input().split()))
    print(filecombine(size))