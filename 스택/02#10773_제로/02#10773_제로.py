import sys
input=sys.stdin.readline
k = int(input())
res=[]
for i in range(k):
    n =int(input())
    if n==0:
        res=res[:-1]
    else:
        res.append(n)
print(sum(res))