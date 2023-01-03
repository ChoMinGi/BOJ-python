import sys

a= int(input())
# 리스트 개수 맞춰주기 위해서
dp=[-1000]
cnt=0
for n in sys.stdin.readline().split():
    # 다음으로 오는 n 값이 더 큰값을 만들어줄수 있는가? 
    dp.append(max(int(dp[cnt])+int(n),int(n)))
    cnt+=1

print(max(dp))