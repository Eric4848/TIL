import sys

N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(N)]

for term in range(1, N):   # 계산할 행렬의 갯수
    for start in range(N):  # 계산할 행렬의 시작점
        if start + term == N:  # 범위를 벗어나면 무시
            break

        dp[start][start + term] = int(1e9)  # 지금 계산할 첫행렬과 끝행렬

        for t in range(start, start + term):   # 시작 - 끝 사이의 한 위치(계산할 행렬의 위치)
            # start ~ t ~ end(start+term)
            dp[start][start + term] = min(dp[start][start + term],
                                          # 👇 행렬 시작~계산할 행렬 위치까지의 최솟값 + 계산할 행렬 다음 ~ 끝행렬까지의 최소값 + 계산할 행렬의 값
                                          dp[start][t] + dp[t + 1][start + term] + arr[start][0] * arr[t][1] *
                                          arr[start + term][1])

print(dp[0][N - 1])


# import sys
#
# input = sys.stdin.readline
# N = int(input())
# mats = []
# nums = []
# dp = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]
#
# for _ in range(N):
#     m, n = map(int, input().split())
#     mats.append((m, n))
#     nums.append(m)
# nums.append(mats[-1][1])
#
# for i in range(1, N+1):
#     dp[i][i] = 0
#
# for i in range(1, N):   # i번째 행렬 곱
#     for j in range(1, N-i+1):   # 계산할 행렬 번호
#         minimum = float('inf')   # 행렬 곱의 최소값을 초기화
#         for k in range(i):   # 계산할 행렬에 이미 계산된 행렬들의 수
#             # j번쨰 까지 행렬들 중 k개의 최소 + j번쨰 부터 행렬들 중 k - 1개 중의 최소 + j행렬 시작 * k번쨰 행렬 * j에서 i번째 뒤 행렬의 열값
#             tmp = dp[j][j+k] + dp[j+k+1][j+i] + nums[j-1] * nums[j+k] * nums[j+i]
#             if tmp < minimum:
#                 minimum = tmp
#         dp[j][j+i] = minimum
#
# print(dp[1][N])
