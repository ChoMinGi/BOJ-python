from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs():
    while q:
        x, y, z = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
                continue
            if box[nz][nx][ny] == -1 or box[nz][nx][ny] == 1:
                continue
            if box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[z][x][y] + 1
                q.append((nx, ny, nz))


m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q = deque()

for z in range(h):
    for x in range(n):
        for y in range(m):
            if box[z][x][y] == 1:
                q.append((x, y, z))

bfs()

max_day = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if box[z][x][y] == 0:
                print(-1)
                exit(0)
            max_day = max(max_day, box[z][x][y])

print(max_day - 1)
