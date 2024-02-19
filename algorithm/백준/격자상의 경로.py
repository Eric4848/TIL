N, M, K = map(int, input().split())
dp = [[0] * M for _ in range(N)]
# 경유 위치 계산 -> 인덱스 계산을 위해 위치-1 기준으로 계산
R = (K - 1) // M
C = (K - 1) % M
if K == 0:   # 경유 위치가 없으면
    R = C = 0   # 0으로 설정

# 시작 위치에서 경유 위치까지 오른쪽, 아래쪽 직선 길의 경우의 수를 1로 설정
for i in range(R+1):
    dp[i][0] = 1
for i in range(C+1):
    dp[0][i] = 1

# 사이 칸들의 이동 경우의 수 계산
for r in range(1, R+1):
    for c in range(1, C+1):
        dp[r][c] = dp[r-1][c] + dp[r][c-1]   # 위칸, 왼쪽칸의 경우의 수의 합

# 경유 위치에서 도착 위치까지 오른쪽, 아래쪽 직선 길의 경우의 수를 경유 위치 까지의 수로 설정
for i in range(R+1, N):
    dp[i][C] = dp[R][C]
for i in range(C+1, M):
    dp[R][i] = dp[R][C]

# 사이 칸들의 이동 경우의 수 계산
for r in range(R+1, N):
    for c in range(C+1, M):
        dp[r][c] = dp[r-1][c] + dp[r][c-1]

print(dp[-1][-1])
