a, b, c = map(int, input().split())
res = 1


def expdiv(res, a, b, c):
    if b == 1:
        res = res * a % c
        return res
    else:
        td = expdiv(res, a, b // 2, c)
        if b % 2 == 0:
            return td * td % c
        else:
            return td * td * a % c


print(expdiv(res, a, b, c))