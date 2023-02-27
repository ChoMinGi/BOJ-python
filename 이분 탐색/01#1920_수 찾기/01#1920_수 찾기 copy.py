# Pypy3로 통과

import sys
input = sys.stdin.readline

input()
a = list(map(int,input().split()))
input()

for i in list(map(int,input().split())):
    if i in a:
        print("1")
    else:
        print("0")