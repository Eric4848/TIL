import sys
from collections import deque

input = sys.stdin.readline
M, N, H = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
answer = -1

dz = [0, 0, 0, 0, 1, -1]
dy = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]

queue = deque()
for i in range(M):
    for j in range(N):
        for k in range(H):
            if matrix[i][j][k] == 1:
                queue.append((i, j, k))

while queue:
    if 0 not in matrix:
        print(0)
    answer += 1
    for _ in range(len(queue)):
        y, x, z = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if -1 < ny < M and -1 < nx < N and -1 < nz < H:
                if matrix[ny][nx][nz] == 0:
                    matrix[ny][nx][nz] = 1
                    queue.append((ny, nx, nz))

check = 0
for mat in matrix:
    if 0 in mat:
        check += 1

if check:
    print(-1)
else:
    print(answer)
