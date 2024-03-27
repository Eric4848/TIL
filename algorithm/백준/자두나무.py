T, W = map(int, input().split())
flag = 1
trees = [0] + [int(input()) for _ in range(T)]
dp = [[0 for _ in range(W+1)] for _ in range(T+1)]   # 이동횟수 + 1(0회 포함)만큼을 나무의 갯수만큼 초기화 한다

dp[1][0] = trees[1] % 2   # 1초일때 이동하지 않은 경우 나머지를 계산하여 1인지 확인
dp[1][1] = trees[1] // 2   # 1초일때 이동한 경우 몫을 계산하여 2인지 확인
for i in range(2, T+1):   # 두번째부터 마지막 나무까지
    for j in range(W+1):   # 0~W번의 이동 별로
        if j % 2 == 0:   # 짝수번 이동했다면
            tmp = trees[i] % 2   # 나머지로 1번나무인지 확인
        else:   # 홀수번 이동했다면
            tmp = trees[i] // 2   # 몫으로 2번나무인지 확인
        dp[i][j] = max(dp[i-1][0:j+1]) + tmp   # 이전 나무의 현 이동횟수만큼 까지의 최대 자두 갯수 중 최대에 현재 먹을 수 있는지 추가

print(max(dp[-1]))   # 마지막 나무에서 최대로 먹을 수 있는 자두 갯수 출력


# 오답
# T, W = map(int, input().split())
# flag = 1
# trees = [0 for _ in range(W+1)]
# for _ in range(T):
#     now = int(input())
#     if flag != now:
#         trees.append(trees[-1] + 1)
#         flag = now
#     else:
#         trees[-1] += 1
#
# for i in range(W+1, len(trees)):
#     trees[i] -= trees[i-W-1]
#
# print(max(trees))
