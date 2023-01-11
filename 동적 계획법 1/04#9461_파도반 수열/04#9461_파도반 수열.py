res = []
pado = [0, 1, 1, 1, 2, 2, 3]

for i in range(7, 101):
    pado.append(pado[i-1]+pado[i-5])

n = int(input())
for i in range(n):
    a = int(input())
    res.append(pado[a])
print(*res, sep='\n')