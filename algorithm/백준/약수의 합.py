# Pypy로 제출
import sys

input = sys.stdin.readline
T = int(input())
nums = [int(input()) for _ in range(T)]
maximum = max(nums)   # 입력값중 최대를 찾아서
dp = [0] * (maximum + 1)   # 0~최대까지 0으로 초기화
for i in range(1, maximum + 1):   # 1부터 최대까지
    # fx계산
    for j in range(i, maximum + 1, i):   # 해당 숫자의 배수마다
        dp[j] += i   # 해당 숫자를 더한다
    # gx계산
    dp[i] += dp[i-1]   # 누적합을 구하기 위해 해당 숫자 이전의 값을 더해준다

for num in nums:
    print(dp[num])
