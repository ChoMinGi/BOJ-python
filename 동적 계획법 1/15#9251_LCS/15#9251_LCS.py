a=list(map(str,input()))
b=list(map(str,input()))

pd = [[0 for n in range(len(b)+1)] for m in range(len(a)+1)]
lcsword = []
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            pd[i+1][j+1]=pd[i][j]+1
            lcsword.append(a[i])
        else:
            pd[i+1][j+1]=max(pd[i][j+1],pd[i+1][j])

print(max(map(max,pd)))
print(lcsword)