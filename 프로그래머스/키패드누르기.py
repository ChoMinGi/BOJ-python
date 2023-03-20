def solution(numbers, hand):
    res = []
    lp = [1, 4]
    rp = [3, 4]
    left = [1, 4, 7]
    right = [3, 6, 9]
    for i in numbers:
        if i == 0:
            i = 11

        h = (i - 1) // 3 + 1
        if i in left:
            lp = [1, h]
            res.append("L")
        elif i in right:
            rp = [3, h]
            res.append("R")
        else:
            ldis = abs(lp[0] - i % 3) + abs(lp[1] - h)
            rdis = abs(rp[0] - i % 3) + abs(rp[1] - h)
            if ldis < rdis:
                lp = [2, h]
                res.append("L")
            elif ldis > rdis:
                rp = [2, h]
                res.append("R")
            else:
                if hand == "right":
                    rp = [2, h]
                    res.append("R")
                else:
                    lp = [2, h]
                    res.append("L")
    result = "".join(res)

    return result
