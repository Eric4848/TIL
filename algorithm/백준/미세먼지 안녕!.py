# 시간 초과
R, C, T = map(int, input().split())
home = [list(map(int, input().split())) for _ in range(R)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
for _ in range(T):
    check = []
    flag = 1
    for r in range(R):
        for c in range(C):
            if 0 < home[r][c]:
                check.append((r, c, home[r][c]))
    for r, c, now in check:
        move = now // 5
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and 0 <= home[nr][nc]:
                home[r][c] -= move
                home[nr][nc] += move

    for r in range(R):
        if home[r][0] == -1:
            if flag:
                flag = 0
                for mr in range(r-1, 0, -1):
                    home[mr][0] = home[mr-1][0]
                for mc in range(C-1):
                    home[0][mc] = home[0][mc+1]
                for mr in range(r):
                    home[mr][C-1] = home[mr+1][C-1]
                for mc in range(C-1, 1, -1):
                    home[r][mc] = home[r][mc-1]
                home[r][1] = 0
            else:
                for mr in range(r+1, R-1):
                    home[mr][0] = home[mr+1][0]
                for mc in range(C-1):
                    home[R-1][mc] = home[R-1][mc+1]
                for mr in range(R-1, r, -1):
                    home[mr][C-1] = home[mr-1][C-1]
                for mc in range(C-1, 1, -1):
                    home[r][mc] = home[r][mc-1]
                home[r][1] = 0

total = 2
for i in range(R):
    total += sum(home[i])
print(total)