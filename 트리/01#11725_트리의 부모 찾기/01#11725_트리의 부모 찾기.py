import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n=int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1 ):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

p =[0]*(n+1)
def dfs(s,tree,p):
    for i in tree[s]:
        if p[i]==0:
            p[i]=s
            dfs(i,tree,p)

dfs(1,tree,p)

print(*p[2:],sep="\n")