n,k=map(int,input().split())
coin=[]
cnt=0
for _ in range(n):
    coin.append(int(input()))
for i in coin[::-1]:
    if i<=k:
        cnt+=k//i
        k=k%i
print(cnt)