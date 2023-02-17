import sys

k = int(input())
draw = []
w = 0
b = 0

for _ in range(k):
    draw += list(map(int, sys.stdin.readline().split()))
print(draw)


def divi(a):
    res = []
    for i in range(2):
        for j in range(2):
            td = []
            for l in range(len(a) // 2):
                td += a[4 * j : 4 * (j + 1)]
            res.append(td)
    return res


def count(qur, w, b):
    for i in qur:
        if 1 not in i:
            w += 1
        elif 0 not in i:
            b += 1
        else:
            count(divi(i), w, b)
    print(w, b)


print(divi(draw))
count(divi(draw), 0, 0)
