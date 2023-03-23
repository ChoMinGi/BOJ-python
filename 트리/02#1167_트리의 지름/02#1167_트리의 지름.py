import sys
from heapq import heappush, heappop

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n):
    td = list(map(int, input().split()))
    for i in range(len(td[1:-1]) // 2):
        tree[td[0]].append((td[i + 1], td[i + 2]))
print(tree)
distance = [[0] * (n + 1) for _ in range(n + 1)]


def dijkstra(dest):
    heap = []
    heappush(heap, (0, dest))
    while heap:
        dist, now = heappop(heap)
        if distance[dest][now] > dist:
            continue
        for i in tree[now]:
            cost = dist + i[1]
            if cost > distance[dest][i[0]]:
                distance[dest][i[0]] = cost
                heappush(heap, (cost, i[0]))
        print(distance)


for i in range(1, n + 1):
    dijkstra(i)

print(distance)
