cntrec = 0
cnt = 0


def fiborec(n):
    global cntrec
    if n == 0 or n == 1:
        cntrec += 1
        return cntrec
    else:
        fiborec(n-1)+fiborec(n-2)
    return cntrec


def fibo(n):
    global cnt
    if fibonum[n] != 0:
        return cnt
    fibonum[n] = fibo(n-1)+fibo(n-2)
    cnt += 1
    return cnt


n = int(input())
fibonum = [0]*n
fibonum[0] = 1
fibonum[1] = 1
print(fiborec(n-1), fibo(n-1)-1)

