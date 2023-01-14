import sys

input = sys.stdin.readline

alist = list(map(ord,input().rstrip()))

cs = [[0 for l in range(len(alist)+1)]for m in range(26)]
cs[alist[0]-97][1]=1

for m in range(26):
    for l in range(2,len(alist)+1):
        cs[m][l]+=cs[m][l-1]
        if alist[l-1]==m+97:
            cs[m][l]+=1
n = int(input())
for i in range(n):
    rep = input().split()
    print(cs[ord(rep[0])-97][int(rep[2])+1]-cs[ord(rep[0])-97][int(rep[1])])
    