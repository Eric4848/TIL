import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]
dists = [[0 for _ in range(N)] for _ in range(N)]   # 각 지점마다 갈 수 있는 최대 거리를 0으로 초기화
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


# 거리 계산
def dfs(r, c):
    if dists[r][c]:   # 이미 거리 계산을 한 지점이면
        return dists[r][c]   # 값을 반환

    dists[r][c] = 1   # 최대거리를 1로 설정
    for i in range(4):   # 4방향으로
        nr = r + dr[i]
        nc = c + dc[i]
        # 다음 위치가 범위 이내, 이전 위치보다 대나무가 더 많다면
        if 0 <= nr < N and 0 <= nc < N and forest[r][c] < forest[nr][nc]:
            dists[r][c] = max(dists[r][c], dfs(nr, nc) + 1)   # 이전 위치의 최대거리와 새로운 위치의 최대거리 + 1 중 큰 것을 저장

    return dists[r][c]   # 최대거리를 반환


# 모든 위치에서 최대거리 계산
answer = 0
for y in range(N):
    for x in range(N):
        answer = max(answer, dfs(y, x))

print(answer)


# 시간 초과
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# N = int(input())
# forest = [list(map(int, input().split())) for _ in range(N)]
# answers = [[0 for _ in range(N)] for _ in range(N)]
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
#
# for y in range(N):
#     for x in range(N):
#         if not answers[y][x]:
#             q = deque([(y, x)])
#             answers[y][x] = 1
#             while q:
#                 r, c = q.popleft()
#                 for i in range(4):
#                     nr = r + dr[i]
#                     nc = c + dc[i]
#                     if 0 <= nr < N and 0 <= nc < N and forest[r][c] < forest[nr][nc] and answers[nr][nc] <= answers[r][c]:
#                         answers[nr][nc] = answers[r][c] + 1
#                         q.append((nr, nc))
#
# answer = 0
# for row in answers:
#     answer = max(answer, max(row))
# print(answer)
