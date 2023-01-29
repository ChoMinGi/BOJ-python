from collections import deque

n, m = map(int, input().split())

sum = 0
queue = deque(range(1, n + 1))
td = 1
loc = list(map(int, input().split()))
cnt = 0
for i in loc:
    n = len(queue)
    if queue[0] == i:
        queue.popleft()
        cnt += 0
    else:
        i = queue.index(i)
        cnt += min(abs(-i), abs(+n - i))
        if abs(-i) < abs(+n - i):
            queue.rotate(-abs(-i))
            queue.popleft()
        else:
            queue.rotate(abs(+n - i))
            queue.popleft()
print(cnt)
