import sys

input = sys.stdin.readline

while 1:
    stc = input().rstrip()
    if stc == ".":
        break
    res = "yes"
    cnt = 0
    cntl = 0
    for i in stc:
        if i == "(":
            cnt += 1
        elif i == ")":
            cnt -= 1
            if cnt < 0 or cntl > 0:
                res = "no"
        if i == "[":
            cntl += 1
        elif i == "]":
            cntl -= 1
            if cntl < 0 or cnt > 0:
                res = "no"
    if (cnt != 0) or (cntl != 0):
        res = "no"
    print(res)
