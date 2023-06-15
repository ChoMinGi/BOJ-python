from collections import deque

# 상자의 크기 입력 받기
m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):  # 네 방향에 대하여 확인
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))


# 이미 익어있는 토마토 위치 찾기
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j))

bfs()

max_day = 0
for row in box:
    if 0 in row:
        print(-1)
        break
    max_day = max(max_day, max(row))
else:
    print(max_day - 1)
