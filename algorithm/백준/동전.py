T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    total = int(input())
    dp = [0 for i in range(total+1)]
    dp[0] = 1
    for i in coins:
        for j in range(1, total+1):
            if j >= i:
                dp[j] += dp[j-i]
    print(dp[total])
