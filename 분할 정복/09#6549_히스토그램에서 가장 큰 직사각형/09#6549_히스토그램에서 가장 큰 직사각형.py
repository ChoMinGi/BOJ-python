# 분할 정복 풀이 (그리디)

import sys
input = sys.stdin.readline


def divandconq(l,r):
    if l==r:
        return tc[l]
    # 가운데있는 부피 최대 구하기
    m=l+(r-l)//2
    lp=m
    rp=m+1
    mH=min(tc[lp],tc[rp])
    mW=2
    mAM=mH*mW

    while (l<lp or rp<r):
        if l==lp:
            rp+=1
            cH=tc[rp]
        elif r==rp:
            lp-=1
            cH=tc[lp]
        elif tc[lp-1] > tc[rp+1]:
            lp-=1
            cH=tc[lp]
        else:
            rp+=1
            cH=tc[rp]
        mH = min(mH,cH)
        mW+=1
        mAM = max(mAM,mH*mW)

    return max(divandconq(l,m),divandconq(m+1,r),mAM)

while 1:
    tc = list(map(int, input().split()))
    if tc[0]==0:
        break
    print(divandconq(1,len(tc)-1))