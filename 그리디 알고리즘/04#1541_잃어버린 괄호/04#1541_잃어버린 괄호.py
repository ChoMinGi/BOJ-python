import sys
math=list(map(str, sys.stdin.readline().rstrip().split("-")))

res=sum(map(int,math[0].split("+")))

for i in math[1:]:
    res-=(sum(map(int,i.split("+"))))
print(res)