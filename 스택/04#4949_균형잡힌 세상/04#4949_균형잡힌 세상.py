import sys

while 1:
    line = sys.stdin.readline().rstrip()
    stack = []
    if line == ".":
        break
    for i in line:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append("]")
                break
        elif i == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")
                break
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
