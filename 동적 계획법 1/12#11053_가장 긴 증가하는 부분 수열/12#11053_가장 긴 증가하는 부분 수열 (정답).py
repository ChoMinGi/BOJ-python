# 정답

n = int(input())
alist=[]
for i in map(int,input().split()):
    alist.append(i)
pd=[1 for m in range(n)]

for j in range(1,n):
    for k in range(j):
        if alist[k]<alist[j]:
            pd[j]=max(pd[k]+1,pd[j])


print(pd)