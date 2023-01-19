import sys

n = int(input())
money=list(map(int, sys.stdin.readline().rstrip().split()))
money = sorted(money)

cnt=0
for j in range(n):
    cnt+=money[j]*(n-j)
print(cnt)