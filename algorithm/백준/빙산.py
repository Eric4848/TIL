# 오답
import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
N, M = map(int, input().split())
ices = [list(map(int, input().split())) for _ in range(N)]
answer = 0
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def count():
    cnt = 0
    for r in range(N):
        for c in range(M):
            if ices[r][c] != 0 and not is_chk[r][c]:
                cnt += 1
                check(r, c)
    return cnt


def check(r, c):
    if ices[r][c] != 0 and not is_chk[r][c]:
        is_chk[r][c] = True
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                check(nr, nc)


def decre():
    for r in range(N):
        for c in range(M):
            if ices[r][c] != 0:
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < N and 0 <= nc < M:
                        if ices[nr][nc] == 0:
                            if 0 < ices[r][c]:
                                ices[r][c] -= 1


while True:
    answer += 1
    total = 0
    is_chk = [[False]*M for _ in range(N)]
    for i in range(N):
        total += sum(ices[i])

    if total == 0:
        answer = 0
        print(answer)
        break

    decre()
    cnt = count()
    if 1 < cnt:
        print(answer)
        break
