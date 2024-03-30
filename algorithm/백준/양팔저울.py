N = int(input())
weights = list(map(int, input().split()))
maximum = sum(weights)   # 추의 모든 무게의 합
total = 2 * maximum + 1   # +, - 방향으로의 모든 무게
dp = [[0 for _ in range(total)] for _ in range(N+1)]   # 양방향 무게만큼 0으로 초기화 해 N+1개 만들어 준다
dp[0][maximum] = 1   # 영점 위치를 1로 변경(무게 잴 수 있음)

for i in range(1, N+1):   # 각 추별로(원 상태를 위해 1~N+1)
    weight = weights[i-1]   # 추의 무게

    # 이전 가능 여부 가졍괴
    for j in range(total):
        dp[i][j] = dp[i-1][j]

    # 추를 원본에 대칭점에 놓는 경우
    for j in range(weight, total):   # 잴 수 있는 무게가 늘어나기 때문에 추의 무게부터 끝까지
        if dp[i-1][j-weight]:   # 이전 결과에서 현재 추 무게만큼 적은 무게를 잴 수 있다면
            dp[i][j] = 1   # 현재 무게를 잴 수 있다
    # 추를 원본에 놓는 경우
    for j in range(0, total-weight):   # 잴 수 있는 무게가 줄어들기 때문에 처음부터 최대-추의 무게까지
        if dp[i-1][j+weight]:   # 이전 결과에서 현재 추 무게만큼 많은 무게를 잴 수 있다면
            dp[i][j] = 1   # 현재 무게를 잴 수 있다

T = int(input())
targets = list(map(int, input().split()))
answers = []
for target in targets:
    # 모든 추의 무게보다 큰경우
    if maximum < target:
        answers.append('N')

    # 무게를 잴 수 있는 경우
    elif dp[-1][maximum + target]:
        answers.append('Y')

    # 무게를 잴 수 없는 경우
    else:
        answers.append('N')

print(*answers)


# N = int(input())
# weights = list(map(int, input().split()))
# maximum = sum(weights) + 1
# dp = [[0 for _ in range(maximum)] for _ in range(N+1)]
#
# for i in range(1, N+1):
#     weight = weights[i-1]
#     for j in range(maximum):
#         dp[i][j] = dp[i-1][j]
#     dp[i][weight] = 1
#
#     for j in range(weight, maximum):
#         if dp[i-1][j-weight]:
#             dp[i][j] = 1
#
#     for j in range(0, maximum-weight):
#         if dp[i-1][j+weight]:
#             dp[i][j] = 1
#
# T = int(input())
# targets = list(map(int, input().split()))
# answers = []
# for target in targets:
#     if dp[-1][target]:
#         answers.append('Y')
#     else:
#         answers.append('N')
#
# print(answers)
