N = int(input())
dp = [1 for _ in range(N)]   # 증가하는 최대 길이를 1로 초기화
nums = [int(input()) for _ in range(N)]

# 가장 길게 증가하는 순서인 아이들 계산
for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))   # 가장 길게 증가하는 순서인 아이를 제외한 나머지 이동
