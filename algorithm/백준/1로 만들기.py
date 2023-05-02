N = int(input())
dp = [0, 0, 1, 1]
for i in range(4, N+1):
    checks = [dp[i - 1] + 1]
    if i % 2 == 0:
        checks.append(dp[i//2] + 1)
    if i % 3 == 0:
        checks.append(dp[i//3] + 1)
    dp.append(min(checks))
print(dp[N])
