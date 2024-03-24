import sys

input = sys.stdin.readline
N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
answer = float('inf')

# 색상별로 첫 집에 색칠하여 계산
for i in range(3):
    dp = [[float('inf') for _ in range(3)] for _ in range(N)]   # 비용을 담을 dp
    dp[0][i] = costs[0][i]   # 첫 집만 계산하는 색을 칠한다
    for j in range(1, N):   # 이후로 각 색상별로 자신이 아닌 이전집들 중 작은 값을 더해준다
        dp[j][0] = costs[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = costs[j][1] + min(dp[j-1][2], dp[j-1][0])
        dp[j][2] = costs[j][2] + min(dp[j-1][0], dp[j-1][1])

    dp[N-1][i] = float('inf')   # 시작집에 비용을 무한으로 늘려 제외
    answer = min(answer, min(dp[N-1]))   # 최소 비용 저장

print(answer)


# import sys
#
# input = sys.stdin.readline
# N = int(input())
# costs = [list(map(int, input().split())) for _ in range(N)]
# dp = [0 for _ in range(3)]
# for i in range(3):
#     dp[i] = costs[0][i]
#     now = i
#     for j in range(1, N-1):
#         if costs[j][(now-1) % 3] < costs[j][(now+1) % 3]:
#             dp[i] += costs[j][(now-1) % 3]
#             now = (now-1) % 3
#         else:
#             dp[i] += costs[j][(now+1) % 3]
#             now = (now+1) % 3
#
#     if i == now:
#         dp[i] += min(costs[N-1][(now+1) % 3], costs[N-1][(now-1) % 3])
#     else:
#         for k in range(3):
#             if k == i or k == now:
#                 continue
#             dp[i] += costs[N-1][k]
#
# print(min(dp))
