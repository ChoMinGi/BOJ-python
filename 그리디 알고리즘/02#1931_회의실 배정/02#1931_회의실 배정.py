import sys

n = int(input())
time =[]
for i in range(n):
    time.append(list(map(int, sys.stdin.readline().rstrip().split())))
time = sorted(time,reverse=True)

td=time[0][0]
cnt=1
for j in range(1,n):
    if time[j][1]<=td:
        cnt+=1
        td=time[j][0]

print(cnt)