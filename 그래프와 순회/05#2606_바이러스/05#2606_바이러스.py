import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)

check = 0


def dfs(s):
    q = deque()
    visited[s] = 1
    q.append(s)
    global check
    while q:
        td = q.popleft()
        for i in graph[td]:
            if visited[i] == 0:
                check += 1
                visited[i] = 1
                q.append(i)


dfs(1)

print(check)
