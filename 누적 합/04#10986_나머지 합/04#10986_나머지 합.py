import sys

n, m = input().split()
a = [0]+list(map(int,sys.stdin.readline().split()))
cs=[0]*int(m)
for i in range(1,len(a)):
    a[i]=(a[i]+a[i-1])%int(m)
    cs[a[i]]+=1
cnt=cs[0]
for j in cs:
    cnt+=int(j*(j-1)/2)

print(cnt)
