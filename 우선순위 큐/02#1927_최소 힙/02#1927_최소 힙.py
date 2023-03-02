import sys
import heapq

input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    td = int(input())
    if td == 0:
        if len(a) != 0:
            print(heapq.heappop(a))
        else:
            print("0")
    else:
        heapq.heappush(a, td)