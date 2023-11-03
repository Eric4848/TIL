# 오답
from collections import deque

N, M, y, x, K = map(int, input().split())
matrix = [list((map(int, input().split()))) for _ in range(N)]
orders = list(map(int, input().split()))
ud_dice = deque([0] * 4)   # 2, 1, 5, 6
lr_dice = deque([0] * 4)   # 4, 1, 3, 6


dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]

for order in orders:

    ny = y + dy[order]
    nx = x + dx[order]

    if 0 <= nx < M and 0 <= ny < N:
        y = ny
        x = nx

        if order == 1:
            lr_dice.appendleft(lr_dice.pop())
            ud_dice[1] = lr_dice[1]
            ud_dice[3] = lr_dice[3]
        if order == 2:
            lr_dice.append(lr_dice.popleft())
            ud_dice[1] = lr_dice[1]
            ud_dice[3] = lr_dice[3]
        if order == 3:
            ud_dice.append(ud_dice.popleft())
            lr_dice[1] = ud_dice[1]
            lr_dice[3] = ud_dice[3]
        if order == 4:
            ud_dice.appendleft(ud_dice.pop())
            lr_dice[1] = ud_dice[1]
            lr_dice[3] = ud_dice[3]

        if matrix[y][x] == 0:
            matrix[y][x] == ud_dice[3]
        else:
            ud_dice[3] = matrix[y][x]
            lr_dice[3] = matrix[y][x]
            matrix[y][x] = 0
        print(ud_dice[1])
