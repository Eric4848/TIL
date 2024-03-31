N = int(input())
healths = list(map(int, input().split()))
joys = list(map(int, input().split()))
dp = [[0 for _ in range(100)] for _ in range(N+1)]   # 최대 체력만큼 N+1개 초기화한다(100을 사용하면 안되므로 idx 99까지)

for i in range(1, N+1):
    health = healths[i-1]
    joy = joys[i-1]

    # 이전 기쁨 정도 가져오기
    for j in range(100):
        dp[i][j] = dp[i-1][j]

    # 현재 인새로 얻는 기쁨과 비교하여 큰 것 저장
    for j in range(health, 100):
        dp[i][j] = max(dp[i][j], dp[i-1][j-health] + joy)

print(dp[-1][-1])
