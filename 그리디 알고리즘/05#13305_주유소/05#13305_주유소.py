import sys

n = int(input())
dtc = list(map(int, sys.stdin.readline().rstrip().split()))
price = list(map(int, sys.stdin.readline().rstrip().split()))
min_price = price[0]
total_price = min_price * dtc[0]
for i in range(1, n - 1):
    if min_price > price[i]:
        min_price = price[i]
    total_price += min_price * dtc[i]

print(total_price)
