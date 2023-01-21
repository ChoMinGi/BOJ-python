import sys

n = int(input())
dtc = list(map(int, sys.stdin.readline().rstrip().split()))
price = list(map(int, sys.stdin.readline().rstrip().split()))
td = 0
cnt = 0
while len(price) != 0:
    td = price.index(min(price))
    cnt += price[td] * sum(dtc[td:])
    price = price[:td]
    dtc = dtc[:td]

print(cnt)
