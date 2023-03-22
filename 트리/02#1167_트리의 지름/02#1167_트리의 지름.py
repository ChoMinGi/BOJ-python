import sys
from heapq import heappush, heappop
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n=int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n):
    td=list(map(int,input().split()))
    for i in range(len(td[1:-1])//2):
        tree[td[0]].append((td[i+1],td[i+2]))
print(tree)

def distra(s):
    heap=[]
    tree[s]
