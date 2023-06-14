import sys
from collections import deque

T = int(sys.stdin.readline().strip())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, visited, field):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if field[nx][ny] and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True


for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().strip().split())
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    count = 0

    for _ in range(K):
        y, x = map(int, sys.stdin.readline().strip().split())
        field[x][y] = 1

    for i in range(N):
        for j in range(M):
            if field[i][j] and not visited[i][j]:
                bfs(i, j, visited, field)
                count += 1
    print(count)
