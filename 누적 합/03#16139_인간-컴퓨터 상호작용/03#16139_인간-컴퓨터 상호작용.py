import sys
input = sys.stdin.readline

cs = [[0]*26]
alist = input().rstrip()

for l in alist:
    addlist = cs[-1][:]
    a = ord(l)-97
    addlist[a]+=1
    print(cs)
    cs.append(addlist)

n = int(input())

for i in range(n):
    w,s,e = input().rstrip().split()
    w = ord(w)-97
    s = int(s)
    e = int(e)
    res = cs[e+1][w]-cs[s][w]

    print(res)