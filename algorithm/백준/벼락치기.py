N, T = map(int, input().split())
chapters = []
for _ in range(N):
    chapters.append(list(map(int, input().split())))

dp = [[0 for _ in range(T+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(T+1):
        dp[i][j] = dp[i-1][j]

    time, score = chapters[i-1]

    for j in range(time, T+1):
        dp[i][j] = max(dp[i][j], dp[i-1][j-time] + score)

print(dp[N][T])


# N, T = map(int, input().split())
# times = []
# scores = []
# for _ in range(N):
#     time, score = map(int, input().split())
#     times.append(time)
#     scores.append(score)
#
# dp = [[0 for _ in range(T+1)] for _ in range(N+1)]
#
# for i in range(1, N+1):
#     for j in range(T+1):
#         dp[i][j] = dp[i-1][j]
#
#     time = times[i-1]
#     score = scores[i-1]
#
#     for j in range(time, T+1):
#         dp[i][j] = max(dp[i][j], dp[i-1][j-time] + score)
#
# print(dp[N][T])
