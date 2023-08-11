N = int(input())
dp = [1] * 10   # 끝자리 수가 0~9 까지 있다, 한자리 적은 숫자의 같은 위치인 경우들 + 같은 자리 숫자의 -1 위치인 경우
for _ in range(1, N):
    for j in range(1, 10):
        dp[j] += dp[j-1]
print(sum(dp))

# N = int(input())
# answer = 1
# for i in range(N):
#     answer = answer * (10 + i) / (i + 1)
# print(int(answer % 10007))
