N = int(input())
# answer matrix[i][j]를 i번째 계산 j가 마지막 숫자로 설정하여 계산
answer = [[0]*10 for _ in range(N)]
# 첫번째 경우 0을 제외한 나머지 숫자들 가능
for i in range(1, 10):
    answer[0][i] = 1
# 그 이후로
for i in range(1, N):
    for j in range(10):
        if j == 0:
            answer[i][j] = answer[i-1][1]
        elif j == 9:
            answer[i][j] = answer[i-1][8]
        else:
            answer[i][j] = answer[i-1][j-1] + answer[i-1][j+1]

print(sum(answer[-1]) % 1000000000)
