N = int(input())
nums = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

cnt = max(dp)   # 최대 갯수를 저장
print(cnt)
answers = []   # 연속된 숫자들을 담을 리스트
for i in range(N-1, -1, -1):   # 역순으로
    if dp[i] == cnt:   # 저장된 dp의 숫자가 최대 숫자 갯수와 같다면 그 수를 사용한 것이므로
        answers.append(nums[i])   # 정답 리스트에 추가
        cnt -= 1   # 최대 갯수 - 1
print(*reversed(answers))
