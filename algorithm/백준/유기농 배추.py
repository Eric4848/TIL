from collections import deque

T = int(input())
answer = [0] * T
for num in range(T):
    c, r, n = map(int, input().split())
    matrix = [[0] * c for _ in range(r)]

    for _ in range(n):
        ic, ir = map(int, input().split())
        matrix[ir][ic] = 1

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]


    def bfs(cr, cc):
        queue = deque()
        queue.append((cr, cc))
        answer[num] += 1
        while queue:
            pr, pc = queue.popleft()
            for i in range(4):
                nr = pr + dr[i]
                nc = pc + dc[i]
                if 0 <= nr < r and 0 <= nc < c:
                    if matrix[nr][nc] == 1:
                        matrix[nr][nc] = 0
                        queue.append((nr, nc))


    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
                bfs(i, j)


for ans in answer:
    print(ans)
