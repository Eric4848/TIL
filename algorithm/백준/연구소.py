# 시간 초과
from collections import deque
import copy

N, M = map(int, input().split())
labs = [list(map(int, input().split())) for _ in range(N)]
answer = 0
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def count(r, c, multi_labs):
    cnt = 1
    q = deque([(r, c)])
    chk = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if multi_labs[nr][nc] == 2:
                    chk = 1

                elif multi_labs[nr][nc] == 0:
                    cnt += 1
                    multi_labs[nr][nc] = 1
                    q.append((nr, nc))
    if chk:
        cnt = 0
    return cnt


def spread():
    global answer
    total = 0
    multi_labs = copy.deepcopy(labs)
    for R in range(N):
        for C in range(M):
            if multi_labs[R][C] == 0:
                multi_labs[R][C] = 1
                total += count(R, C, multi_labs)
    answer = max(answer, total)


def build_wall(cnt):
    if cnt == 3:
        spread()
        return

    for r in range(N):
        for c in range(M):
            if labs[r][c] == 0:
                labs[r][c] = 1
                build_wall(cnt + 1)
                labs[r][c] = 0


build_wall(0)
print(answer)


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
