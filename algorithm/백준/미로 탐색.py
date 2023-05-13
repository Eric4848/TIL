# bfs
from collections import deque

r, c = map(int, input().split())
matrix = []
for _ in range(r):
    matrix.append(list(map(int, input())))


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or c <= nx or ny < 0 or r <= ny:
                continue

            if matrix[ny][nx] == 0:
                continue

            if matrix[ny][nx] == 1:
                matrix[ny][nx] = matrix[y][x] + 1
                queue.append((nx, ny))

    print(matrix[r-1][c-1])


bfs(0, 0)


# dfs - 시간 초과
# r, c = map(int, input().split())
# matrix = []
# answer = [float('INF')]
# for _ in range(r):
#     temp = []
#     for maze in input():
#         temp.append(int(maze))
#     matrix.append(temp)
#
#
# def dfs(cr, cc, move):
#
#     if move > answer[0]:
#         return
#
#     if cr == r-1 and cc == c-1:
#         if move < answer[0]:
#             answer[0] = move
#         return
#
#     if cr+1 < r and matrix[cr+1][cc] == 1:
#         matrix[cr + 1][cc] = 0
#         dfs(cr+1, cc, move+1)
#         matrix[cr + 1][cc] = 1
#
#     if cr-1 >= 0 and matrix[cr-1][cc] == 1:
#         matrix[cr - 1][cc] = 0
#         dfs(cr-1, cc, move+1)
#         matrix[cr - 1][cc] = 1
#
#     if cc+1 < c and matrix[cr][cc+1] == 1:
#         matrix[cr][cc+1] = 0
#         dfs(cr, cc+1, move+1)
#         matrix[cr][cc+1] = 1
#
#     if cc-1 >= 0 and matrix[cr][cc-1] == 1:
#         matrix[cr][cc-1] = 0
#         dfs(cr, cc-1, move+1)
#         matrix[cr][cc-1] = 1
#
#
# dfs(0, 0, 0)
#
# print(answer[0]+1)
