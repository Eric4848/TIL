import sys
from collections import deque

input = sys.stdin.readline
M, N, H = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
answer = -1

dz = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dx = [0, 0, 0, 0, 1, -1]

queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if matrix[i][j][k] == 1:
                queue.append((i, j, k))

while queue:
    answer += 1
    for _ in range(len(queue)):
        z, y, x= queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if -1 < nz < H and -1 < ny < M and -1 < nx < N:
                if matrix[nz][ny][nx] == 0:
                    matrix[nz][ny][nx] = 1
                    queue.append((nz, ny, nx))

check = 0
for matz in matrix:
    for maty in matz:
        if 0 in maty:
            check += 1

if check:
    print(-1)
else:
    print(answer)
