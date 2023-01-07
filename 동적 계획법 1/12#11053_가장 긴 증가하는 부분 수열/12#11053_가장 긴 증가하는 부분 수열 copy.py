n = int(input())
alist=[]
for i in map(int,input().split()):
    alist.append(i)
pd = [1]*(n+1)
td = alist[0]
for i in range(1,n+1):
    if alist[i-1]>td:
        td=alist[i-1]
        pd[i]+=pd[i-1]
    else:
        td=alist[i-1]

print(pd)