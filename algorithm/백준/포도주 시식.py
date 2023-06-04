N = int(input())
dp = [0]*N
wines = [int(input()) for _ in range(N)]

if N < 3:
    print(sum(wines))
else:
    dp[0] = wines[0]
    for i in range(1, N):
        dp[i] = max(dp[i-3]+wines[i]+wines[i-1], dp[i-2]+wines[i], dp[i-1])
    print(dp[-1])
