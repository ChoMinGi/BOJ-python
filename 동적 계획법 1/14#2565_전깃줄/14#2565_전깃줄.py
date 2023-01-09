n = int(input())
a={}
alist=[]

# 딕셔너리 형태로 저장
for i in range(n):
    k,v = input().split()
    a[int(k)] = int(v)
# sorted 와 비슷한 형태
for i in range(1,501):
    if i in a:
        alist.append(a[i])

# 다만 pd의 리스트 개수를 n개로 데이터 세이브
pd=[1 for m in range(n)]

for j in range(1,n):
    for k in range(j):
        if alist[k]<alist[j]:
            pd[j]=max(pd[k]+1,pd[j])


print(n-max(pd))