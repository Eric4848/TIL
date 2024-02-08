import sys

input = sys.stdin.readline
N, S, M = map(int, input().split())
volumes = list(map(int, input().split()))
answer = -1   # 정답을 -1로 초기화(불가능할 시)
# dp 사용 / 시작 1 + 곡수만큼 최대볼륨+1(0~최대) 0으로 초기화 한다
dp = [[0] * (M+1) for _ in range(N+1)]
dp[0][S] = 1   # 시작 시점에 볼륨 칸을 1로 변경

for i in range(N):   # 곡 시작할 때마다
    if not sum(dp[i]):   # 현재 순서에 가능한 볼륨이 없으면
        break   # 종료

    for j in range(M+1):   # 모든 가능 볼륨만큼(0~최대)
        if dp[i][j]:   # 현재 볼륨을 사용할 수 있다면
            if 0 <= j - volumes[i]:   # 볼륨을 줄여도 0이상이면
                dp[i+1][j-volumes[i]] = 1   # 다음 순서 줄인 볼륨을 1로 변경

            if j + volumes[i] <= M:   # 볼륨을 키워도 최대 이하면
                dp[i+1][j+volumes[i]] = 1   # 다음 순서 키운 볼륨을 1로 변경


for i in range(M+1):   # 사용가능한 볼륨별로
    if dp[N][i]:   # 마지막 순서에 사용할 수 있는 볼륨이면
        answer = i   # 정답을 해당 볼륨으로 변경

print(answer)


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# N, S, M = map(int, input().split())
# volumes = list(map(int, input().split()))
# answer = -1
#
#
# def change(v, d):
#     global answer
#     if d == N:
#         answer = max(answer, v)
#         return
#
#     if v+volumes[d] <= M:
#         change(v+volumes[d], d+1)
#
#     if 0 <= v-volumes[d]:
#         change(v-volumes[d], d+1)
#
#
# change(S, 0)
# print(answer)
