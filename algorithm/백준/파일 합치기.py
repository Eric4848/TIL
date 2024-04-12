T = int(input())
for _ in range(T):
    K = int(input())
    pages = list(map(int, input().split()))
    dp = [[0 for _ in range(K)] for _ in range(K)]   # r ~ c까지의 합을 0으로 초기화
    # 시작 지점에서 뒤로 하나씩 더해나간다
    for i in range(K-1):   # 시작 지점(두개를 더해야 하므로 -1
        dp[i][i+1] = pages[i] + pages[i+1]   # 시적 위치 + 그 뒤
        for j in range(i+2, K):   # 시작위치 다다음부터 끝까지
            dp[i][j] = dp[i][j-1] + pages[j]   # 이전 값과 현재 페이지를 더해준다

    # 효율적인 것 먼저 더하기
    for i in range(2, K):   # 더할 숫자들의 갯수 -1(idx로 계산하므로 1 적은 수)
        for j in range(K-i):   # 더할 숫자들의 맨 앞 위치
            # 더하기 시작위치부터 i+1개까지의 합의 최소값은 사이의 j ~ k의 합 + k+1 ~ i+j의 합의 최소값
            dp[j][i+j] += min([dp[j][k] + dp[k+1][i+j] for k in range(j, i+j)])

    print(dp[0][-1])
 