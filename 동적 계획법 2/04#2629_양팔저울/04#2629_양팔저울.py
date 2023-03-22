w = int(input())
wlist = list(map(int, input().split()))

m = int(input())
mlist = list(map(int, input().split()))

res = [[0] * 40001 for _ in range(w + 1)]
for i in range(1, w + 1):
    td = wlist[i - 1]
    res[i][td] = 1
    for j in range(1, 40001):
        if res[i - 1][j] != 0:
            res[i][j] = 1
            res[i][abs(j + td)] = 1
            res[i][abs(j - td)] = 1

result = []
for k in mlist:
    if res[w][k] == 1:
        result.append("Y")
    else:
        result.append("N")

print(*result)
