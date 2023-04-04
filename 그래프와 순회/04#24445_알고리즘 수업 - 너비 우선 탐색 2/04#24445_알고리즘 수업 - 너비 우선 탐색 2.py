import sys
from collections import deque

input = sys.stdin.readline

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1,n+1):
    graph[i].sort(reverse=True)


cnt=1
def bfs(start):
    q = deque()
    visited[start]=1
    q.append(start)
    global cnt
    while q:
        td =q.popleft()
        for i in graph[td]:
            if visited[i]==0:
                cnt+=1
                visited[i]=cnt
                q.append(i)


bfs(r)

print(*visited[1:],sep='\n')