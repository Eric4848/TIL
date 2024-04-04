N, M = map(int, input().split())
profits = [[0 for _ in range(M)]]   # 투자금액 0일때 수익을 기업 수만큼 초기화
answer = 0
invest = []

for _ in range(N):   # 투자금액별로
    profit = list(map(int, input().split()))
    profits.append(profit[1:])   # 회사별 수익을 추가(금액별로 입력되기 때문)

dp = [[0 for _ in range(N+1)] for _ in range(M+1)]   # 총 수익을 0으로 최대 투자금 + 1만큼 기업 수 + 1만큼 초기화한다 ([기업 번호 0~M][투자한 금액 0~N] 크기)
invests = [[[0 for _ in range(M)] for _ in range(N+1)] for _ in range(M+1)]   # 투자금액 정보를 기업 수만큼, 총 수익과 같은 크기로 초기화한다 ([각 기업별 투자액][기업 번호][투자한 금액])

for i in range(1, M+1):   # 각 기업별로
    # 이전 투자 정보 가져오기
    for j in range(N+1):
        dp[i][j] = dp[i-1][j]
        invests[i][j] = invests[i-1][j][:]
    # 이번 기업의 투자 금액별 수익 계산
    for j in range(0, N+1):   # 기업에 투자할 금액
        for k in range(j, N+1):   # 투자 가능한 범위
            if dp[i][k] < dp[i-1][k-j] + profits[j][i-1]:   # 현재 수익보다 투자했을 때 수익이 크다면
                dp[i][k] = dp[i-1][k-j] + profits[j][i-1]   # 수익 갱신
                invests[i][k] = invests[i-1][k-j][:]   # 투자금액 정보를 현기업 투자 전 정보를 가져온다
                invests[i][k][i-1] = j   # 투자금액 정보의 현  기업 위치 값을 투자 금액으로 갱신
                answer = max(answer, dp[i][k])   # 정답과 비교하여 큰 것 설정

print(answer)
print(*invests[M][N])


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
