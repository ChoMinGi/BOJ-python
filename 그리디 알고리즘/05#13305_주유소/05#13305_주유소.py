import sys

n = int(input())
dtc=list(map(int, sys.stdin.readline().rstrip().split()))
price=list(map(int, sys.stdin.readline().rstrip().split()))
min_price = price[:-2]
total_price=0
cnt=0
for i in range(2,n-1):
    if min_price>=price[n-i]:
        total_price+=dtc[n-i]
        min_price=price[n-i]

print(cnt)