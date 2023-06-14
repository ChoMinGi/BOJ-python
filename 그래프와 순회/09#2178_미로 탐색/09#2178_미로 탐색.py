from collections import deque

# 미로의 크기 입력 받기
n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

# 이동할 네 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 함수 정의
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):  # 네 방향에 대하여 확인
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:  # 미로 찾기 공간을 벗어난 경우 무시
                continue
            if maze[nx][ny] == 0:  # 벽인 경우 무시
                continue
            if maze[nx][ny] == 1:  # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[n - 1][m - 1]  # 가장 오른쪽 아래까지의 최단 거리 반환


print(bfs(0, 0))  # BFS를 수행한 결과 출력
