# 스택 풀이

import sys
input = sys.stdin.readline

def stack(list):

    rec=[]
    recMA=0

    for h in list:
        cnt = 0
        while len(rec) != 0 and rec[-1][1] > h:
            # cnt는 현재 높이의 히스토그램이 앞으로 총 몇칸이 유효한지를 나타낸다.
            cnt += rec[-1][0]
            recMA = max(recMA, cnt * rec[-1][1])
            rec.pop()

        cnt += 1
        rec.append([cnt,h])

    cnt = 0
    while len(rec) != 0:
        cnt += rec[-1][0]
        recMA = max(recMA, cnt*rec[-1][1])
        rec.pop()

    return recMA

while 1:
    tc = list(map(int, input().split()))
    if tc[0]==0:
        break
    print(stack(tc[1:]))