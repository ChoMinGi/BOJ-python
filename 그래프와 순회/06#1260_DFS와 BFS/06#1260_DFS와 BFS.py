import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visitedDfs = [0] * (n + 1)
visitedBfs = [0] * (n + 1)

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, n + 1):
    graph[i].sort()

dfs_res = []
bfs_res = []


def dfs(graph, v, visitedDfs):
    global dfs_res
    visitedDfs[v] = 1
    dfs_res.append(v)
    for i in graph[v]:
        if visitedDfs[i] == 0:
            dfs(graph, i, visitedDfs)


def bfs(start):
    global bfs_res
    q = deque()
    q.append(start)
    visitedBfs[start] = 1
    bfs_res.append(start)
    while q:
        td = q.popleft()
        for i in graph[td]:
            if visitedBfs[i] == 0:
                visitedBfs[i] = 1
                bfs_res.append(i)
                q.append(i)


dfs(graph, v, visitedDfs)
bfs(v)

print(*dfs_res)
print(*bfs_res)
