import sys

input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    td = int(input())
    if td == 0:
        if len(a) != 0:
            print(a.pop(a.index(max(a))))
        else:
            print("0")
    else:
        a.append(td)
