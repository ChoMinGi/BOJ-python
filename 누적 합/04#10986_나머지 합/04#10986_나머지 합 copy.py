import sys
from collections import Counter
input = sys.stdin.readline
n, m = map(int, input().split())
li = list(map(int, input().split()))
li[0] = li[0]%m
for i in range(1, n):
    li[i] = (li[i-1] + li[i]) % m
    print(li[i])
li = Counter(li)
print(li,li[0])
answer = li[0]
for v in li.values():
    answer += v*(v-1)//2
print(answer)