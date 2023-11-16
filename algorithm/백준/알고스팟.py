# 메모리 초과
import sys

sys.setrecursionlimit(10 ** 9)
N, M = map(int, input().split())
mat = [list(map(int, input().rstrip())) for _ in range(M)]
answer = [N + M]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def move(r, c, crash):
    if answer[0] < crash:
        return

    if r == M-1 and c == N-1:
        answer[0] = min(answer[0], crash)
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < M and 0 <= nc < N:
            if mat[nr][nc] == 1:
                move(nr, nc, crash+1)
            else:
                move(nr, nc, crash)


move(0, 0, 0)
print(answer[0])


# 시간 초과
# import sys
#
# sys.setrecursionlimit(10 ** 9)
# N, M = map(int, input().split())
# mat = [list(map(int, input().rstrip())) for _ in range(M)]
# answer = [N + M]
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
# is_visit = [[False] * N for _ in range(M)]
# is_visit[0][0] = True
#
#
# def move(r, c, crash):
#     if answer[0] <= crash:
#         return
#
#     if r == M-1 and c == N-1:
#         answer[0] = min(answer[0], crash)
#         return
#
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < M and 0 <= nc < N and not is_visit[nr][nc]:
#             is_visit[nr][nc] = True
#             if mat[nr][nc] == 1:
#                 move(nr, nc, crash+1)
#             else:
#                 move(nr, nc, crash)
#             is_visit[nr][nc] = False
#
#
# move(0, 0, 0)
# print(answer[0])


# 시간 초과
# import copy
# import sys
#
# sys.setrecursionlimit(10 ** 9)
# N, M = map(int, input().split())
# mat = [list(map(int, input().rstrip())) for _ in range(M)]
# answer = [N + M]
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
# is_visit = [[False] * N for _ in range(M)]
# is_visit[0][0] = True
#
#
# def move(r, c, crash, visit):
#     if answer[0] < crash:
#         return
#
#     if r == M-1 and c == N-1:
#         answer[0] = min(answer[0], crash)
#         return
#
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < M and 0 <= nc < N and not visit[nr][nc]:
#             tmp = copy.deepcopy(visit)
#             tmp[nr][nc] = True
#             if mat[nr][nc] == 1:
#                 move(nr, nc, crash+1, tmp)
#             else:
#                 move(nr, nc, crash, tmp)
#
#
# move(0, 0, 0, is_visit)
# print(answer[0])
