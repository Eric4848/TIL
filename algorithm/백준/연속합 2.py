import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
dp = [[0] * N for _ in range(2)]   # 제거하지 않은 경우, 제거한 경우
dp[0][0] = nums[0]   # 제거하지 않은 경우 초기값 설정
dp[1][0] = nums[0]   # 제거한 경우 초기값 설정
for i in range(1, N):   # 두번째부터
    # 제거하지 않는 경우 현위치 숫자와 현위치 숫자 + 이전까지의 합 중 큰 것 저장
    dp[0][i] = max(nums[i], nums[i] + dp[0][i-1])
    # 제거하는 경우 현재 위치를 제거한 값(제거하지 않은 숫자 기준)과 제거한 후에 더해오던 값 + 현위치 숫자 중 큰 것 저장
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + nums[i])
answer = max(max(dp[0]), max(dp[1]))

print(answer)


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# N = int(input())
# nums = list(map(int, input().split()))
# dp = [0] * N
# dp[0] = nums[0]
# for i in range(1, N):
#     dp[i] = max(nums[i], nums[i] + dp[i-1])
# answer = max(dp)
#
# chks = [0]
# for i in range(N):
#     if nums[i] < 0:
#         dp = [0] * N
#         dp[0] = nums[0]
#         for j in range(1, N):
#             if j == i:
#                 dp[j] = dp[j-1]
#                 continue
#             dp[j] = max(nums[j], nums[j] + dp[j - 1])
#         answer = max(answer, max(dp))
#
# print(answer)
