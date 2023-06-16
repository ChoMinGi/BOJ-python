from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, list(input().strip()))) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs():
    queue = deque()
    queue.append((0, 0, 1))  # Start from top-left with a chance to break a wall
    visited[0][0][1] = 1
    while queue:
        x, y, broke = queue.popleft()
        if x == n - 1 and y == m - 1:  # If we reached the destination
            return visited[x][y][broke]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 1 and broke:  # If there's a wall and we can break it
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    queue.append((nx, ny, 0))
                elif (
                    grid[nx][ny] == 0 and visited[nx][ny][broke] == 0
                ):  # If the path is not visited
                    visited[nx][ny][broke] = visited[x][y][broke] + 1
                    queue.append((nx, ny, broke))
    return -1


print(bfs())
