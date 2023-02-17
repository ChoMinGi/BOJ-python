import sys

k = int(input())
draw = []
w = 0
b = 0

for _ in range(k):
    draw.append(list(map(int, sys.stdin.readline().split())))

print(draw)


def count(x, y, n):
    global w, b
    color = draw[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != draw[i][j]:
                count(x, y, n // 2)
                count(x, y + n // 2, n // 2)
                count(x + n // 2, y, n // 2)
                count(x + n // 2, y + n // 2, n // 2)
                return

    if color == 0:
        w += 1
    else:
        b += 1


count(0, 0, k)
print(w, b, sep="\n")
