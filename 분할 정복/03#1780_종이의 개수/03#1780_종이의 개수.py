import sys

k = int(input())
draw = []
res = []
m = 0
z = 0
p = 0
for _ in range(k):
    draw.append(list(map(int, sys.stdin.readline().split())))


def count(x, y, n):
    global m, z, p
    color = draw[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != draw[i][j]:
                t = n // 3
                count(x, y, t)
                count(x, y + t, t)
                count(x, y + (2 * t), t)
                count(x + t, y, t)
                count(x + t, y + t, t)
                count(x + t, y + (2 * t), t)
                count(x + (2 * t), y, t)
                count(x + (2 * t), y + t, t)
                count(x + (2 * t), y + (2 * t), t)
                return

    if color == 0:
        z += 1
    elif color == 1:
        p += 1
    else:
        m += 1


count(0, 0, k)
print(m, z, p, sep="\n")
