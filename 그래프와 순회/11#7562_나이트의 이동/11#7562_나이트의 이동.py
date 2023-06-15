from collections import deque


dx = [2, 1, -1, -2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1, y1))

    while queue:
        x, y = queue.popleft()
        if x == x2 and y == y2:
            print(visited[x][y] - 1)
            return

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= m:  # 미로 찾기 공간을 벗어난 경우 무시
                continue
            if visited[nx][ny] == 0:  # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    return


n = int(input())

for i in range(n):
    m = int(input())
    visited = [[0] * m for _ in range(m)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    visited[x1][y1] = 1
    bfs(x1, y1, x2, y2)
