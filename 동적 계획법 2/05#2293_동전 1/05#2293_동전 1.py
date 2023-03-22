import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))

res = [0 for _ in range(k + 1)]
res[0] = 1

for i in a:
    for j in range(i, k + 1):
        if j - i >= 0:
            res[j] += res[j - i]

print(res[k])
