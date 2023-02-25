import sys
from collections import deque
input = sys.stdin.readline

def stack(list):
    cnt=0
    rec=deque()
    recMA=0

    for i in list[1:]:
        while len(rec)>0:
            ltd=rec[-1]
            if i < ltd[1]:
                rec.pop()
                recMA=max(recMA, (cnt-ltd[0])*ltd[1], (ltd[0]-len(rec)+1)*ltd[1] )
        cnt+=1
        rec.append([cnt,i])
    cnt+=1

    while len(rec)>1 :
        pos=rec.pop()
        recMA=max(recMA, (cnt-pos[0])*pos[1], (pos[0]*pos[1]))
    
    j=rec.pop()
    recMA=max(recMA, (cnt-j[0])*j[1])

    return recMA
                
while 1:
    tc = list(map(int, input().split()))
    if tc[0]==0:
        break
    print(stack(tc[1:]))