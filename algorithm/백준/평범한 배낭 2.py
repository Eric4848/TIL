# 메모리 초과
N, M = map(int, input().split())

weights = [0]
satisfactions = [0]
counts = [0]
T = 0
for _ in range(N):
    V, C, K = map(int, input().split())
    weights.append(V)
    satisfactions.append(C)
    counts.append(K)
    T += K

dp = [[0 for _ in range(M+1)] for _ in range(T+1)]
key = 0

for i in range(1, N+1):
    weight = weights[i]
    satisfaction = satisfactions[i]
    count = counts[i]
    key -= 1
    for _ in range(count):
        key += 1
        for j in range(M+1):
            dp[i+key][j] = dp[i+key-1][j]

        for j in range(weight, M+1):
            if dp[i+key][j] < dp[i+key-1][j-weight] + satisfaction:
                dp[i+key][j] = dp[i+key-1][j-weight] + satisfaction
print(dp[T][M])


# 메모리 초과
# N, M = map(int, input().split())
#
# weights = [0]
# satisfactions = [0]
#
# for _ in range(N):
#     V, C, K = map(int, input().split())
#     for _ in range(K):
#         weights.append(V)
#         satisfactions.append(C)
#
# T = len(weights)
# dp = [[0 for _ in range(M+1)] for _ in range(T)]
#
# for i in range(1, T):
#     weight = weights[i]
#     satisfaction = satisfactions[i]
#
#     for j in range(M+1):
#         dp[i][j] = dp[i-1][j]
#
#     for j in range(weight, M+1):
#         if dp[i][j] < dp[i-1][j-weight] + satisfaction:
#             dp[i][j] = dp[i-1][j-weight] + satisfaction
#
# print(dp[T-1][M])
