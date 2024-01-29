import sys

input = sys.stdin.readline
N = int(input())
dp = [0] * (N + 1)   # 정답을 계산할 dp 리스트를 0으로 초기화, +1은 계산을 위해
tables = [list(map(int, input().split())) for _ in range(N)]

for i in range(N-1, -1, -1):   # 날짜의 역순으로
    if N < tables[i][0] + i:   # 그날 상담을 했을 때 가능한 날짜를 초과하면
        dp[i] = dp[i+1]   # 그 다음날의 계획을 가져온다 -> dp애소 1개 더 만든 이유
    else:   # 상담이 가능하다면
        dp[i] = max(dp[i+1], dp[i + tables[i][0]] + tables[i][1])   # 그 다음날의 상담결과, 오늘 상담 후 끝난 날 상담결과 중 큰 것 저장

print(dp[0])   # 맨 첫날의 계획 출력
