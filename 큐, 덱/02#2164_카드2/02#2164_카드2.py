from collections import deque

n = int(input())
queue = deque(range(1, n + 1))
while len(queue) > 1:
    queue.popleft()
    k = queue.popleft()
    queue.append(k)

print(*queue)
