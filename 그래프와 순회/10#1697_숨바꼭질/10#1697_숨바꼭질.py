import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())


def bfs():
    d = deque()
    d.append(n)
    tdlist = [0] * (100001)
    while d:
        td = d.popleft()
        if td == k:
            print(tdlist[td])
            break
        for i in [td - 1, td + 1, td * 2]:
            if 0 <= i <= 100000 and not tdlist[i]:
                tdlist[i] = tdlist[td] + 1
                d.append(i)


bfs()
