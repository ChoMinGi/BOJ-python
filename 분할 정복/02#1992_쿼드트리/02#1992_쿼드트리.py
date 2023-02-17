import sys

k = int(input())
draw = []
res = []

for _ in range(k):
    a = sys.stdin.readline().rstrip()
    draw.append(list(map(int, str(a))))


def count(x, y, n):
    global w, b
    color = draw[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != draw[i][j]:
                res.append("(")
                count(x, y, n // 2)
                count(x, y + n // 2, n // 2)
                count(x + n // 2, y, n // 2)
                count(x + n // 2, y + n // 2, n // 2)
                res.append(")")
                return

    if color == 0:
        res.append("0")
    else:
        res.append("1")


count(0, 0, k)
print(*res, sep="")
