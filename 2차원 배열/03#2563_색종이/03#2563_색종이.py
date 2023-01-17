n= int(input())

ab=[[0]*100 for _ in range(100)]
for _ in range(n):
    x, y = input().split()
    x=int(x)
    y=int(y)
    for i in range(x,x+10):
        for j in range(y,y+10):
            ab[i][j]=1

print(sum(map(sum,ab)))