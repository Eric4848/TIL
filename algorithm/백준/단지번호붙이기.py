from collections import deque

N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
answer = []
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(sr, sc):
    matrix[sr][sc] = 0
    queue = deque()
    queue.append((sr, sc))
    cnt = 0
    while queue:
        qr, qc = queue.popleft()
        cnt += 1
        for i in range(4):
            nr = qr + dr[i]
            nc = qc + dc[i]
            if nr < 0 or N <= nr or nc < 0 or N <= nc:
                continue

            if matrix[nr][nc] == 1:
                queue.append((nr, nc))
                matrix[nr][nc] = 0
    answer.append(cnt)


for r in range(N):
    for c in range(N):
        if matrix[r][c] == 1:
            bfs(r, c)

answer.sort()
print(len(answer))
for ans in answer:
    print(ans)
