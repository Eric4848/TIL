# 오답
import sys

sys.setrecursionlimit(10 ** 9)
N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
answer = 0


def move(r, c):
    total.append(A[r][c])
    chk.append((r, c))
    is_able[r][c] = False
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if nr == N or nc == N or nr == -1 or nc == -1:
            return
        if is_able[nr][nc]:
            if L <= abs(A[r][c] - A[nr][nc]) <= R:
                move(nr, nc)


while True:
    flag = 0
    print(A)
    is_able = [[True] * N for _ in range(N)]
    for i in range(N - 1):
        for j in range(N - 1):
            if is_able[i][j]:
                total = []
                chk = []
                move(i, j)
                if 2 < len(total):
                    flag = 1
                shared = sum(total) // len(total)
                for rr, rc in chk:
                    A[rr][rc] = shared
    if not flag:
        print(answer)
        break
    else:
        answer += 1
