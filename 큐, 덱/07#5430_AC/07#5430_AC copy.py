from collections import deque

t = int(input())
for _ in range(t):
    func = list(map(str, input().strip()))
    n = int(input())
    try:
        lst = deque(map(int, input().strip("[]").split(",")))
        cnt = 1
        for i in func:
            if i == "R":
                cnt *= -1
            else:
                if cnt > 0:
                    lst.popleft()
                else:
                    lst.pop()
        lst = str(list(lst)[::cnt])
        print(lst.replace(" ", ""))
    except:
        print("error")
