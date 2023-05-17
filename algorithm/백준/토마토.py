from collections import deque

c, r = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]

answer = -1
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

queue = deque()
for i in range(r):
    for j in range(c):
        if matrix[i][j] == 1:
            queue.append((i, j))

while queue:
    answer += 1
    for _ in range(len(queue)):
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if -1 < ny < r and -1 < nx < c:
                if matrix[ny][nx] == 0:
                    matrix[ny][nx] = 1
                    queue.append((ny, nx))

check = 0
for mat in matrix:
    if 0 in mat:
        check += 1

if check:
    print(-1)
else:
    print(answer)
