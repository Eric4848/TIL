N, M = map(int, input().split())
profits = [[0 for _ in range(M)]]
answer = 0
loc = []
maximum = 0

for _ in range(N):
    profit = list(map(int, input().split()))
    profit = profit[1:]
    profits.append(profit)
    maximum += max(profit)

dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
locs = [[[0 for _ in range(M)] for _ in range(N+1)] for _ in range(M+1)]

for i in range(1, M+1):
    for j in range(N+1):
        dp[i][j] = dp[i-1][j]
        locs[i][j] = locs[i-1][j]
    for j in range(1, N+1):
        for k in range(j, N+1):
            if dp[i][j] < dp[i-1][k-j] + profits[j][i-1]:
                dp[i][j] = dp[i-1][k-j] + profits[j][i-1]


for d in dp:
    print(*d)

print(profits)
# for loc in locs:
#     print(loc)

print(answer)
print(*locs)


# 2개의 회사인 경우
# N, M = map(int, input().split())
# compa = [0]
# compb = [0]
# answer = 0
# loc = []
#
# for _ in range(N):
#     i, a, b = map(int, input().split())
#     compa.append(a)
#     compb.append(b)
#
# dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
#
# for i in range(N+1):
#     for j in range(i, N+1):
#         dp[i][N-j] = compa[i]
#
# for j in range(N+1):
#     for i in range(j, N+1):
#         dp[N-i][j] += compb[j]
#         if answer < dp[N-i][j]:
#             answer = dp[N-i][j]
#             loc = [N-i, j]
#
# print(answer)
# print(*loc)
