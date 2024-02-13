N = int(input())
nums = list(map(int, input().split()))
dp = [[0] * 21 for _ in range(N-1)]   # 마지막 등호 전까지 계산하므로 0으로초기화된 21칸 리스트를 N-1개 생성한다
dp[0][nums[0]] = 1   # 맨 처음 시작 숫자를 1로 변경한다

for i in range(N-2):   # 연산 갯수만큼
    for j in range(21):   # 사용 가능한 숫자에서
        if dp[i][j]:   # 만들 수 있는 수라면
            if 0 <= j - nums[i+1]:   # 다음 숫자를 뺀 것이 0 이상이라면
                if not dp[i+1][j-nums[i+1]]:   # 계산된 적 없다면
                    dp[i+1][j-nums[i+1]] = dp[i][j]   # 이전까지 갯수 저장
                else:   # 계산된 적 있다면
                    dp[i+1][j-nums[i+1]] += dp[i][j]   # 이전까지 갯수 더해준다

            if j + nums[i+1] <= 20:   # 다음 숫자를 더한것이 20 이하라면
                if not dp[i+1][j+nums[i+1]]:   # 뺄때와 동일하다
                    dp[i+1][j+nums[i+1]] = dp[i][j]
                else:
                    dp[i+1][j+nums[i+1]] += dp[i][j]

print(dp[-1][nums[-1]])   # 최종 결과의 등호 뒤 숫자칸을 출력한다
