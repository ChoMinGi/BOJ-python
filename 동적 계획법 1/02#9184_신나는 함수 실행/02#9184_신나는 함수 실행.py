def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    elif stg[a][b][c] != 0:
        return stg[a][b][c]

    elif a < b and b < c:
        stg[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return stg[a][b][c]
    else:
        stg[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + \
            w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return stg[a][b][c]


result = []
stg = [[[0]*(21) for _ in range(21)] for _ in range(21)]
i = 0

while i == 0:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        i = 1
    else:
        result.append(f'w({a}, {b}, {c}) = {w(a,b,c)}')
print(*result, sep='\n')