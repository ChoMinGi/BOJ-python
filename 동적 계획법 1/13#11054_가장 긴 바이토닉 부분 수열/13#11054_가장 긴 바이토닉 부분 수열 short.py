n = int(input())
a=list(map(int,input().split()))
ra=a[::-1]
pu=[1]*n
pdd=[1]*n
pd=[-1]*n
for j in range(1,n):
    for k in range(j):
        if a[k]<a[j]:
            pu[j]=max(pu[k]+1,pu[j])
        if ra[k]<ra[j]:
            pdd[j]=max(pdd[k]+1,pdd[j])
pdd = pdd[::-1]
for l in range(n):
    pd[l]+=pu[l]+pdd[l]
print(max(pd))