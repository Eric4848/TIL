# 시간 내
import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    seaList = []

    while q:
        x, y = q.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny]:
                    sea += 1
                elif graph[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
        if sea > 0:
            seaList.append((x, y, sea))
    for x, y, sea in seaList:
        graph[x][y] = max(0, graph[x][y] - sea)

    return 1


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ice.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
year = 0

while ice:
    visited = [[0] * m for _ in range(n)]
    delList = []
    group = 0
    for i, j in ice:
        if graph[i][j] and not visited[i][j]:
            group += bfs(i, j)
        if graph[i][j] == 0:
            delList.append((i, j))
    if group > 1:
        print(year)
        break
    ice = sorted(list(set(ice) - set(delList)))
    year += 1

if group < 2:
    print(0)


# 시간 초과
# import sys
#
# sys.setrecursionlimit(10 ** 9)
# input = sys.stdin.readline
# N, M = map(int, input().split())
# ices = [list(map(int, input().split())) for _ in range(N)]
# answer = 0
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
#
#
# def count():
#     cnt = 0
#     for r in range(N):
#         for c in range(M):
#             if ices[r][c] != 0 and not is_chk[r][c]:
#                 cnt += 1
#                 check(r, c)
#     return cnt
#
#
# def check(r, c):
#     if ices[r][c] != 0 and not is_chk[r][c]:
#         is_chk[r][c] = True
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nr < N and 0 <= nc < M:
#                 check(nr, nc)
#
#
# def decre():
#     temp = [[0] * M for _ in range(N)]
#     for r in range(N):
#         for c in range(M):
#             if ices[r][c] != 0:
#                 temp[r][c] = ices[r][c]
#                 for i in range(4):
#                     nr = r + dr[i]
#                     nc = c + dc[i]
#                     if 0 <= nr < N and 0 <= nc < M:
#                         if ices[nr][nc] == 0:
#                             if 0 < temp[r][c]:
#                                 temp[r][c] -= 1
#     return temp
#
#
# while True:
#     answer += 1
#     total = 0
#     is_chk = [[False] * M for _ in range(N)]
#     for i in range(N):
#         total += sum(ices[i])
#
#     if total == 0:
#         answer = 0
#         print(answer)
#         break
#
#     ices = decre()
#     cnt = count()
#     if 1 < cnt:
#         print(answer)
#         break
