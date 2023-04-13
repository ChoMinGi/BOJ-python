import sys
from heapq import heappush, heappop

input = sys.stdin.readline

V, E = map(int, input().split())
k = int(input())
INF = 1000000000

graph = [[] * (V + 1) for _ in range(V + 1)]
distance = [INF] * (V + 1)

for _ in range(V):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(dest):
    heap = []
    heappush(heap, (0, dest))
    distance[dest] = 0

    while heap:
        dist, now = heappop(heap)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(heap, (cost, i[0]))


dijkstra(k)

for i in range(1, V + 1):
    res = distance[i]
    if res == INF:
        print("INF")
    else:
        print(res)
