import sys

input = sys.stdin.readline
N, M = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for r in range(N):
    for c in range(N):
        dp[r+1][c+1] = dp[r][c+1] + dp[r+1][c] - dp[r][c] + nums[r][c]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    answer = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(answer)


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# nums = [[0] + list(map(int, input().split())) for _ in range(N)]
#
# for r in range(N):
#     for c in range(N):
#         nums[r][c+1] += nums[r][c]
#
# for _ in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     answer = 0
#     for r in range(x1-1, x2):
#         answer = answer + nums[r][y2] - nums[r][y1-1]
#     print(answer)
