from collections import deque

n, m = map(int, input().split())

sum = 0
queue = deque(range(n))
td = 1
loc = list(map(int, input().split()))
for i in loc:
    sum += min(abs(td - i), abs(td + n - i))

    td = i
