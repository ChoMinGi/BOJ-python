from collections import deque
import copy

tc = int(input())

for i in range(tc):
    n, m = map(int, input().split())
    ipt = deque(map(int, input().split()))
    cnt = 1
    while len(ipt) >= 1:
        maxipt = max(ipt)
        if maxipt == ipt[0]:
            if m == 0:
                print(cnt)
                break
            ipt.popleft()
            m -= 1
            cnt += 1
        else:
            td = ipt.popleft()
            ipt.append(td)
            m -= 1
        if m < 0:
            m = len(ipt) - 1
