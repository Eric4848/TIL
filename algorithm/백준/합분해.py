N, K = map(int, input().split())
answer = [[[] for _ in range(N)] for _ in range(K)]   # N+1열을 K행만큼 만들어준다

for i in range(N):   # 행은 숫자의 갯수
    answer[0][i] = 1   # 첫행에는 1을 넣어주고
for j in range(K):   # 열은 주어진 정수
    answer[j][0] = j+1   # 첫 열에는 1부터 1씩 늘려가며 넣어준다

for i in range(1, K):   # 둘째행부터 마지막 행까지
    for j in range(1, N):   # 둘째열부터 마지막 행까지
        answer[i][j] = answer[i-1][j]+answer[i][j-1]   # 해당 갯수는 한행 위 갯수 + 한 열 왼쪽 갯수
print(answer[-1][-1] % 1000000000)

# 시간초과
# N, K = map(int, input().split())
# answer = [0]
#
#
# def num(cnt, total):
#     if cnt == K:
#         if total == N:
#             answer[0] += 1
#         return
#
#     for i in range(N+1):
#         num(cnt + 1, total + i)
#
#
# num(0, 0)
# print(answer[0] % 1000000000)
