def solution(expression):
    res = []
    mid = ["+", "-", "*"]
    case = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
    for j in case:
        a = list(expression.split(mid[j[0]]))
        b = [i.split(mid[j[1]]) for i in a]
        res.append(mid[j[2]].join(str(eval(b))))
        print(res)
    return


print(solution("100-200*300-500+20"))
