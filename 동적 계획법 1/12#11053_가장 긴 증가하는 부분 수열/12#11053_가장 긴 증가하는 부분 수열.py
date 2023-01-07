n = int(input())
cnt = 0
td = 0
alist=[[1 for i in range(2)] for j in range(n)]
for i in map(int,input().split()):
    alist[cnt][0] = i
    cnt+=1

max = 0
pd = 0

for i in range(n):
    if alist[i][0] > alist[pd][0] and alist[i][0] > alist[max][0]:
        max=i
        alist[i][1]+=alist[max][1]
    elif alist[i][0] > alist[pd][0]:
        pd=i
        alist[i][1]+=alist[pd][1]
    else:
        pd = i

print(*alist)