import sys

a= int(input())
res= -1000
cnt =0
for n in sys.stdin.readline().split():
    # 양수 더하기
    cnt += int(n)
    # 만들어진 양수가 기존 최대값보다 큰가?
    res = max(cnt, res)
    # 일종의 양수 음수 필터라고 생각해도 좋다. 음수면 0으로 리셋
    cnt = max(cnt,0)

print(res)