N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
length = sum(costs) + 1   # 비용의 총합 + 1 길이 계산
answer = float('inf')

dp = [[0 for _ in range(length)] for _ in range(N+1)]   # 길이만큼 초기화 한 행을 앱 갯수 + 1개 만들어준다
for i in range(1, N+1):   # 1  ~ N까지 (앱 번호)
    memory = memories[i-1]
    cost = costs[i-1]

    # 이전의 값 계승
    for j in range(length):
        dp[i][j] = dp[i-1][j]

    # 현재 앱을 종료할 지 결정
    for j in range(cost, length):   # 현재 앱을 제거하는 비용 ~ 최대비용까지
        dp[i][j] = max(dp[i-1][j-cost] + memory, dp[i][j])   # 이전 계산에서 현재 비용만큼 적은 시점의 확보 메모리 + 현재 메모리 , 계승해온 현재 위치의 메모리 중 큰 것 선택
        if M <= dp[i][j]:   # 현재 확보한 메모리가 기준치보다 크면
            answer = min(answer, j)   # 정답과 현재 비용을 비교하여 적은 것 저장

print(answer)
