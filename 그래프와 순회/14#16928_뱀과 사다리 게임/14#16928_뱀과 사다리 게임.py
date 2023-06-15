from collections import deque

# 이동 횟수를 저장하는 list를 -1로 초기화
dist = [-1] * 101
# 뱀과 사다리를 저장하는 list를 0으로 초기화
move = [0] * 101

n, m = map(int, input().split())
for _ in range(n + m):
    x, y = map(int, input().split())
    move[x] = y

dist[1] = 0
q = deque()
q.append(1)
while q:
    x = q.popleft()
    for i in range(1, 7):
        y = x + i
        if y > 100:
            continue
        if move[y] != 0:
            y = move[y]
        if dist[y] == -1:
            dist[y] = dist[x] + 1
            q.append(y)

print(dist)
