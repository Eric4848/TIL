C, N = map(int, input().split())
costs = []
customers = []
answer = float('inf')

for _ in range(N):
    cost, customer = map(int, input().split())
    costs.append(cost)
    customers.append(customer)

maximum = C * max(costs) + 1   # 비용 최대치를 비용의 최대 * 원하는 고객 수 + 1로 설정
dp = [[0 for _ in range(maximum)] for _ in range(N+1)]   # 최대비용만큼 N+1개 생성

for i in range(1, N+1):
    cost = costs[i-1]
    customer = customers[i-1]

    # 이전 결과값 가져오기
    for j in range(maximum):
        dp[i][j] = dp[i-1][j]

    # 이번 지역 홍보 계산
    for j in range(cost, maximum):   # 이번 지역 홍보 비용부터 끝까지
        dp[i][j] = max(dp[i][j], dp[i][j-cost] + customer)   # 홍보 했을 때 더 많은 고객을 저장(반복이 가능하므로 현재 지역 기준)
        if C <= dp[i][j]:   # 조건을 충족한다면
            answer = min(answer, j)   # 비용의 최소값을 저장

print(answer)
