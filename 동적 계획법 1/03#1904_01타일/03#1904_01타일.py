n = int(input())
res = [0]*1000001
res[0] = 1
res[1] = 1
for i in range(2, n+1):
    res[i] = res[i-1]+res[i-2]
    res[i] = res[i] % 15746
print(res[n])