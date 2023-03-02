import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
res = [a[0]]


def LIS_binary(end, td):
    s = 0
    e = end
    while s <= e:
        mid = (s + e) // 2
        if res[mid] >= td:
            tr = mid
            e = mid - 1
        else:
            s = mid + 1
    res[tr] = td


for i in range(1, len(a)):
    if res[-1] < a[i]:
        res.append(a[i])
    else:
        LIS_binary(len(res) - 1, a[i])

print(res)
