N = int(input())   # 총 숫자의 갯수
A = list(map(int, input().split()))   # 숫자들
dp = [1] * N   # 총 숫자 수 만큼 가장 긴 부분이 감소하는 갯수를 1로 초기화해서 만들어준다
for i in range(N):   # 뒷숫자
    for j in range(i):   # 앞숫자
        if A[i] < A[j]:   # 뒷숫자가 앞숫자보다 작으면
            dp[i] = max(dp[i], dp[j] + 1)   # 뒷숫자까지 갯수와 앞숫자까지 갯수 + 1개 중 큰것을 뒷숫자 갯수에 저장한다
print(max(dp))   # 감소갯수들 중 가장 큰 값을 출력한다
