from collections import deque

stack = deque()
n = int(input())
t = 1
ans = []
cnnt = 0

for i in range(n):
    a = int(input())
    if a >= t:
        while a >= t:
            stack.append(t)
            ans.append("+")
            t += 1
        stack.pop()
        ans.append("-")
    else:
        if stack[-1] == a:
            stack.pop()
            ans.append("-")
        else:
            cnnt = 1

if cnnt == 0:
    print(*ans, sep="\n")
else:
    print("NO")
