from collections import deque

n, k = map(int, input().split())

cirqueue = deque(range(1, n + 1))
resqueue = deque()

while len(cirqueue) >= 1:
    cirqueue.rotate(-k + 1)
    resqueue.append(cirqueue.popleft())

print("<", end="")
print(*resqueue, sep=", ", end="")
print(">")
