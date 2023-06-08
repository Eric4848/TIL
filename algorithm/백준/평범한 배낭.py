# 냅색 알고리즘(물건을 나눌 수 없는 경우)
N, K = map(int, input().split())
stuffs = [list(map(int, input().split())) for _ in range(N)]   # W, V
dp = [[0] * (K+1) for _ in range(N)]   # K개는 반드시 1개 추가 > 물품 개수가 여러개일 때 계산을 위해
for i in range(N):   # y축은 종류
    for j in range(1, K+1):   # x축은 무게
        W = stuffs[i][0]   # 물건의 무게
        V = stuffs[i][1]   # 물건의 가치

        if j < W:   # 무게가 버틸수 있는 무게보다 무거우면
            dp[i][j] = dp[i-1][j]   # 그 물건을 담기 전의 총 가치를 저장
        else:
            dp[i][j] = max(V+dp[i-1][j-W], dp[i-1][j])   # 물건을 담을 때와 버릴 때 중 더 가치가 큰 값 저장

print(dp[-1][-1])
