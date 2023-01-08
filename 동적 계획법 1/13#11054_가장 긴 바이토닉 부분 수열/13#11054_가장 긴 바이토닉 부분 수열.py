n = int(input())
alist=list(map(int,input().split()))
rev_alist = alist[::-1]

pdu=[1 for m in range(n)]
pdd=[1 for m in range(n)]
pd=[0]*n

for j in range(1,n):
    for k in range(j):
        if alist[k]<alist[j]:
            pdu[j]=max(pdu[k]+1,pdu[j])
        if rev_alist[k]<rev_alist[j]:
            pdd[j]=max(pdd[k]+1,pdd[j])

pdd = pdd[::-1]
for l in range(n):
    pd[l]=pdu[l]+pdd[l]-1

print(max(pd))