import sys

k = int(input())
draw = []

for _ in range(k):
    draw.append(list(map(int, sys.stdin.readline().split())))


def divi(list, k):
    res = []
    for i in range(2):
        for j in range(2):
            td = []
            for l in range(k // 2):
                td += list[4 * i + l][4 * j : 4 * (j + 1)]
            res.append(td)
    return res


def count(qur):
    global w, b
    for i in qur:
        if 1 not in i:
            w += 1
        elif 0 not in i:
            b += 1
        else:
            count(divi(i, k // 2))
    print(w, b)


count(draw)
