import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)

check = 

def dfs(s):


dfs(1)
