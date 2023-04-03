import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1,n+1):
    graph[i].sort()

cnt = 1
print(graph)
def dfs(graph, v, visited):
    global cnt
    visited[v]=cnt
    for i in graph[v]:
        if visited[i]==0:
            cnt+=1
            dfs(graph,i,visited)

dfs(graph,r,visited)

print(*visited[1:],sep='\n')