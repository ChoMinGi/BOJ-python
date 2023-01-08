# 리스트에 번호를 저장하는 것이 아니라 번호를 index로 1을 저장한다.

n = int(input())
alist=[0]*1001
for i in map(int,input().split()):
    alist[i] = max(alist[:i])+1

print(max(alist))
