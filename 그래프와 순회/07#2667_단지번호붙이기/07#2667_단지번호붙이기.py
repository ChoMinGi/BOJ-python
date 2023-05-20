import sys
from collections import deque

around = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs(i, j, graph):
    n = len(graph)
    q = deque()
    q.append((i, j))
    graph[i][j] = 0
    cnt = 1
    while q:
        td = q.popleft()
        for i in around:
            tdx = i[0] + td[0]
            tdy = i[1] + td[1]
            if tdx < 0 or tdy < 0 or tdx >= n or tdy >= n:
                continue
            if graph[tdx][tdy] == 1:
                graph[tdx][tdy] = 0
                q.append((tdx, tdy))
                cnt += 1
    return cnt


input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))


res = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            res.append(bfs(i, j, graph))


res.sort()
print(len(res))
for i in range(len(res)):
    print(res[i])
