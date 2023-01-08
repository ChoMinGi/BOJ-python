n = int(input())
pd=[0]*n
each=[]
row=[0]*n
for i in range(n):
    each.append(int(input()))

pd[0] = each[0]
if n>1:
    pd[1] = each[0]+each[1]
if n>2:
    pd[2] = max(each[2]+each[1],each[2]+each[0],pd[1])
for i in range(3,n):
    row[i]=each[i]+each[i-1]
    pd[i] = max(each[i]+pd[i-2],pd[i-1],row[i]+pd[i-3])

print(pd[0:2])
print(pd[n-1])