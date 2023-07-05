N = int(input())
# schedules = [[0, 0]]
# for _ in range(N):
#     schedules.append(list(map(int, input().split())))
# print(schedules)

schedules = [list(map(int, input().split())) for _ in range(N)]   # 인덱싱을 0부터 진행(1일치 -> 0번 인덱스)
dp = [0] * (N+1)   # 최댓값을 저장하기 위한 배열(계산을 위해 1개 더 생성)
for i in range(N-1, -1, -1):   # 뒤에서부터 하나씩 앞으로 계산(i-1일차)
    if i + schedules[i][0] > N:   # i-1일 + i-1일의 상담 기간이 총 근무기간+1보다 크면
        dp[i] = dp[i+1]   # 이전(뒷날)의 값 저장
    else:
        dp[i] = max(dp[i+1], schedules[i][1] + dp[i + schedules[i][0]])   # 이전의 값과 오늘 상담을 하고 상담기간 후의 값을 비교하여 더 큰 값 저장
print(dp[0])   # 0번째 값을 출력
