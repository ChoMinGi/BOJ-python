import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[str(0)] * (n + 1)]
visited = [[0] * (n + 1) for i in range(n + 1)]

for _ in range(n):
    graph.append(list("0" + str(input().rstrip())))

print(visited, graph)

res = []
around = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            cnt += 1
            q = deque()
            q.append((i, j))
            while q:
                td = q.popleft()
                for i in around:
                    tdx = i[0] + td[0]
                    tdy = i[1] + td[1]

        res.append(cnt)
        cnt = 0
