import sys
from collections import deque

n = int(input())
queue = deque()
for i in range(n):
    a = sys.stdin.readline().rstrip().split()
    if a[0] == "push_front":
        queue.appendleft(a[1])
    elif a[0] == "push_back":
        queue.append(a[1])
    elif a[0] == "size":
        print(len(queue))
    elif a[0] == "empty":
        if len(queue) == 0:
            print("1")
        else:
            print("0")
    elif len(queue) == 0:
        print("-1")
    elif a[0] == "pop_front":
        print(queue.popleft())
    elif a[0] == "pop_back":
        print(queue.pop())
    elif a[0] == "front":
        print(queue[0])
    elif a[0] == "back":
        print(queue[-1])
