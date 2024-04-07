N, M = map(int, input().split(' '))

dp = [0 for _ in range(M + 1)]   # 가방에 담을 수 있는 무게 + 1만큼 초기화
objects = []   # 물건들의 정보를 담을 리스트

for _ in range(N):
    W, C, K = map(int, input().split(' '))
    # 이진법과 유사하게 2의 배수들로 최대 수 계산
    idx = 1   # 2진수의 자리
    while 0 < K:   # 들고갈 수 있는 갯수가 있다면
        m = min(idx, K)   # 계산할 수 를 K와 2진수 자리 중 작은 것으로 선택
        objects.append((W * m, C * m))   # 선택값을 무게와 만족도에 각각 곱해 저장
        K -= idx   # K에서 2진수 자리를 뺴준다(K가 선택 된 경우 0이 되므로 반복문 종료는 동일)
        idx *= 2   # 2진수의 자리를 2배로 늘려준다

for W, C in objects:   # 물건들의 무게와 만족도별로
    for i in range(M, W - 1, -1):   # 최대 무게에서 담을 수 있는 무게까지
        dp[i] = max(dp[i], dp[i - W] + C)   # 현재와 담는 것 중 큰 것 선택

print(dp[M])

# 시간 초과
# import sys
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# dp = [0 for _ in range(M+1)]
# weights = []
# satisfactions = []
#
# for _ in range(N):
#     V, C, K = map(int, input().split())
#     idx = 1
#     while 0 < K:
#         tmp = min(idx, K)
#
#         weights.append(V * tmp)
#         satisfactions.append(C * tmp)
#
#         idx *= 2
#         K -= tmp
#
# for i in range(len(weights)):
#     for j in range(M, 0, -1):
#         if weights[i] <= j:
#             dp[j] = max(dp[j], dp[j-weights[i]] + satisfactions[i])
#
# print(dp[M])


# 메모리 초과
# N, M = map(int, input().split())
#
# weights = [0]
# satisfactions = [0]
# counts = [0]
# T = 0
# for _ in range(N):
#     V, C, K = map(int, input().split())
#     weights.append(V)
#     satisfactions.append(C)
#     counts.append(K)
#     T += K
#
# dp = [[0 for _ in range(M+1)] for _ in range(T+1)]
# key = 0
#
# for i in range(1, N+1):
#     weight = weights[i]
#     satisfaction = satisfactions[i]
#     count = counts[i]
#     key -= 1
#     for _ in range(count):
#         key += 1
#         for j in range(M+1):
#             dp[i+key][j] = dp[i+key-1][j]
#
#         for j in range(weight, M+1):
#             if dp[i+key][j] < dp[i+key-1][j-weight] + satisfaction:
#                 dp[i+key][j] = dp[i+key-1][j-weight] + satisfaction
# print(dp[T][M])


# 메모리 초과
# N, M = map(int, input().split())
#
# weights = [0]
# satisfactions = [0]
#
# for _ in range(N):
#     V, C, K = map(int, input().split())
#     for _ in range(K):
#         weights.append(V)
#         satisfactions.append(C)
#
# T = len(weights)
# dp = [[0 for _ in range(M+1)] for _ in range(T)]
#
# for i in range(1, T):
#     weight = weights[i]
#     satisfaction = satisfactions[i]
#
#     for j in range(M+1):
#         dp[i][j] = dp[i-1][j]
#
#     for j in range(weight, M+1):
#         if dp[i][j] < dp[i-1][j-weight] + satisfaction:
#             dp[i][j] = dp[i-1][j-weight] + satisfaction
#
# print(dp[T-1][M])
