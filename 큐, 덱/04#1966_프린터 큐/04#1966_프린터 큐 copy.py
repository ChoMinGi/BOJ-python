from collections import deque
import copy

tc = int(input())

for i in range(tc):
    n, m = map(int, input().split())
    ipt = deque(map(int, input().split()))
    cnt = 0
    for j in copy.deepcopy(ipt):
        if max(ipt) > j:
            pl = ipt.popleft()
            ipt.append(pl)
        else:
            ipt.popleft
            cnt += 1
    print(cnt)
