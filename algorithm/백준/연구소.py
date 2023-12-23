from sys import stdin
from collections import deque
from copy import deepcopy
from itertools import combinations


# 안전 지역을 세는 bfs
def bfs(graph):
    q = deque([(j, i) for i in range(N) for j in range(M) if graph[i][j] == 2])   # 바이러스가 있는 지점을 큐에 추가
    while q:
        x, y = q.popleft()
        for nx, ny in zip([x + 1, x - 1, x, x], [y, y, y + 1, y - 1]):   # 4방향으로
            if 0 <= nx < M and 0 <= ny < N and not graph[ny][nx]:   # 범위 이내이며 빈공간이면
                graph[ny][nx] = 2   # 바이러스에 감염되고
                q.append((nx, ny))    # 큐에 해당 위치 추가

    global answer
    count = sum([i.count(0) for i in graph])   # 각 줄별로 0을 세어 더한다
    answer = max(answer, count)   # 정답과 비교하여 큰 것 저장


N, M = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(N)]
x_y = [(x, y) for x in range(M) for y in range(N) if not graph[y][x]]   # 빈칸인 가로, 세로의 위치들을 저장
answer = 0   # 정답을 0으로 초기화

for c in combinations(x_y, 3):   # 조합을 이용하여 빈 곳 3개 선택
    tmp_graph = deepcopy(graph)   # 연구실을 deepcopy로 복제하고
    for x, y in c:   # 선택된 빈 곳 3곳에
        tmp_graph[y][x] = 1   # 벽을 세운다
    bfs(tmp_graph)   # 안전지역을 세준다

print(answer)


# 시간 초과
# from collections import deque
# import copy
#
# N, M = map(int, input().split())
# labs = [list(map(int, input().split())) for _ in range(N)]
# answer = 0
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
#
#
# def count(r, c, multi_labs):
#     cnt = 1
#     q = deque([(r, c)])
#     chk = 0
#     while q:
#         r, c = q.popleft()
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nr < N and 0 <= nc < M:
#                 if multi_labs[nr][nc] == 2:
#                     chk = 1
#
#                 elif multi_labs[nr][nc] == 0:
#                     cnt += 1
#                     multi_labs[nr][nc] = 1
#                     q.append((nr, nc))
#     if chk:
#         cnt = 0
#     return cnt
#
#
# def spread():
#     global answer
#     total = 0
#     multi_labs = copy.deepcopy(labs)
#     for R in range(N):
#         for C in range(M):
#             if multi_labs[R][C] == 0:
#                 multi_labs[R][C] = 1
#                 total += count(R, C, multi_labs)
#     answer = max(answer, total)
#
#
# def build_wall(cnt):
#     if cnt == 3:
#         spread()
#         return
#
#     for r in range(N):
#         for c in range(M):
#             if labs[r][c] == 0:
#                 labs[r][c] = 1
#                 build_wall(cnt + 1)
#                 labs[r][c] = 0
#
#
# build_wall(0)
# print(answer)


# 시간 초과
# from collections import deque
# import copy
#
# N, M = map(int, input().split())
# labs = [list(map(int, input().split())) for _ in range(N)]
# answer = 0
# virus = []
# for r in range(N):
#     for c in range(M):
#         if labs[r][c] == 2:
#             virus.append((r, c))
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
#
#
# def spread():
#     global answer
#     q = deque(copy.deepcopy(virus))
#     multi_labs = copy.deepcopy(labs)
#     while q:
#         r, c = q.popleft()
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nr < N and 0 <= nc < M and multi_labs[nr][nc] == 0:
#                 multi_labs[nr][nc] = 2
#                 q.append((nr, nc))
#
#     cnt = 0
#     for r in range(N):
#         for c in range(M):
#             if multi_labs[r][c] == 0:
#                 cnt += 1
#     answer = max(answer, cnt)
#
#
# def build_wall(cnt):
#     if cnt == 3:
#         spread()
#         return
#
#     for r in range(N):
#         for c in range(M):
#             if labs[r][c] == 0:
#                 labs[r][c] = 1
#                 build_wall(cnt + 1)
#                 labs[r][c] = 0
#
#
# build_wall(0)
# print(answer)
