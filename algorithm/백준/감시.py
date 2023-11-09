# 오답
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
camera = []
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def count():
    counts = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                counts += 1
    return counts


answer = [count()]
for i in range(N):
    for j in range(M):
        if 0 < matrix[i][j] < 6:
            camera.append((i, j, matrix[i][j]))


def dfs(d):
    if d == cams:
        answer[0] = min(answer[0], count())
        print(matrix)
        return
    r, c, a = camera[d]
    if a == 1:
        for i in range(4):
            nr = r
            nc = c
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 0:
                        matrix[nr][nc] = 7
                    nr += dr[i]
                    nc += dc[i]
            dfs(d+1)
            nr = r
            nc = c
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 7:
                        matrix[nr][nc] = 0
                    nr += dr[i]
                    nc += dc[i]

    elif a == 2:
        for i in range(2):
            nr = r
            nc = c
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 0:
                        matrix[nr][nc] = 7
                    nr += dr[i]
                    nc += dc[i]
            nr = r
            nc = c
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 0:
                        matrix[nr][nc] = 7
                    nr += dr[i + 2]
                    nc += dc[i + 2]
            dfs(d+1)
            nr = r
            nc = c
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 7:
                        matrix[nr][nc] = 0
                    nr += dr[i]
                    nc += dc[i]
            nr = r
            nc = c
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 7:
                        matrix[nr][nc] = 0
                    nr += dr[i + 2]
                    nc += dc[i + 2]

    elif a == 3:
        for i in range(4):
            nr = r
            nc = c
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 0:
                        matrix[nr][nc] = 7
                    nr += dr[i]
                    nc += dc[i]
            nr = r
            nc = c
            nxt = (i + 1) % 4
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 0:
                        matrix[nr][nc] = 7
                    nr += dr[nxt]
                    nc += dc[nxt]
            dfs(d + 1)
            nr = r
            nc = c
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 7:
                        matrix[nr][nc] = 0
                    nr += dr[i]
                    nc += dc[i]
            nr = r
            nc = c
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 7:
                        matrix[nr][nc] = 0
                    nr += dr[nxt]
                    nc += dc[nxt]

    elif a == 4:
        for i in range(4):
            nr = r
            nc = c
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 0:
                        matrix[nr][nc] = 7
                    nr += dr[i]
                    nc += dc[i]
            nr = r
            nc = c
            nxt = (i + 1) % 4
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 0:
                        matrix[nr][nc] = 7
                    nr += dr[nxt]
                    nc += dc[nxt]
            nr = r
            nc = c
            nxt2 = (i + 2) % 4
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 0:
                        matrix[nr][nc] = 7
                    nr += dr[nxt2]
                    nc += dc[nxt2]
            dfs(d + 1)
            nr = r
            nc = c
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 7:
                        matrix[nr][nc] = 0
                    nr += dr[i]
                    nc += dc[i]
            nr = r
            nc = c
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 7:
                        matrix[nr][nc] = 0
                    nr += dr[nxt]
                    nc += dc[nxt]
            nr = r
            nc = c
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 7:
                        matrix[nr][nc] = 0
                    nr += dr[nxt2]
                    nc += dc[nxt2]

    elif a == 5:
        for i in range(4):
            nr = r
            nc = c
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 0:
                        matrix[nr][nc] = 7
                    nr += dr[i]
                    nc += dc[i]
            nr = r
            nc = c
            nxt = (i + 1) % 4
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 0:
                        matrix[nr][nc] = 7
                    nr += dr[nxt]
                    nc += dc[nxt]
            nr = r
            nc = c
            nxt2 = (i + 2) % 4
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 0:
                        matrix[nr][nc] = 7
                    nr += dr[nxt2]
                    nc += dc[nxt2]
            nr = r
            nc = c
            nxt3 = (i + 3) % 4
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 0:
                        matrix[nr][nc] = 7
                    nr += dr[nxt3]
                    nc += dc[nxt3]
            dfs(d + 1)
            nr = r
            nc = c
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 7:
                        matrix[nr][nc] = 0
                    nr += dr[i]
                    nc += dc[i]
            nr = r
            nc = c
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 7:
                        matrix[nr][nc] = 0
                    nr += dr[nxt]
                    nc += dc[nxt]
            nr = r
            nc = c
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 7:
                        matrix[nr][nc] = 0
                    nr += dr[nxt2]
                    nc += dc[nxt2]
            nr = r
            nc = c
            while 0 <= nr < N and 0 <= nc < M:
                if matrix[nr][nc] == 6:
                    break
                else:
                    if matrix[nr][nc] == 7:
                        matrix[nr][nc] = 0
                    nr += dr[nxt3]
                    nc += dc[nxt3]


cams = len(camera)
dfs(0)
print(answer[0])
