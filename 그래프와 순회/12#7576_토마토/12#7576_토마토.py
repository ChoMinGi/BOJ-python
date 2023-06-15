from collections import deque

n, m = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(m)]

ripen = []
for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            ripen.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 함수 정의
def bfs(ripe):
    count = 0
    while ripe:
        next_ripe = []
        for x, y in ripe:
            for i in range(4):  # 네 방향에 대하여 확인
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if tomato[nx][ny] == -1:
                    continue
                if tomato[nx][ny] == 0:
                    next_ripe.append((nx, ny))
                    tomato[nx][ny] = 1

        if not next_ripe:
            break
        ripe = next_ripe
        count += 1

    for row in tomato:
        if 0 in row:
            return -1
    return count


print(bfs(ripen))
