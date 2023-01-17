import sys
input = sys.stdin.readline

ab=[]
for _ in range(9):
    ab.append(list(map(int,input().split())))

max=0
x=0
y=0
for i in range(9):
    for j in range(9):
        if ab[i][j]>=max:
            x,y=i+1,j+1
            max=ab[i][j]
print(max)
print(x,y)