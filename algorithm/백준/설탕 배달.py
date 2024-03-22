N = int(input())
dp = [float('inf') for _ in range(N+1)]   # 입력 인덱스까지 무한으로 초기화한 dp생성

# 3보다 작은경우 제외
if 3 <= N:
    dp[3] = 1
# 5보다 작은경우 제외
if 5 <= N:
    dp[5] = 1

# 6부터 입력된 숫자째 인덱스까지
for i in range(6, N+1):
    # 3 이전 + 1, 5이전 + 1 중 작은 것 선택(3짜리 추가, 5짜리 추가
    dp[i] = min(dp[i-3] + 1, dp[i-5] + 1)

if dp[N] == float('inf'):
    print(-1)
else:
    print(dp[N])
