import sys

input = sys.stdin.readline

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

n, m, x, y, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))
dice = [0] * 6   # 3, 4, 2, 5, 1, 6

for d in orders:
    nx = x + dx[d]
    ny = y + dy[d]

    if not 0 <= nx < n or not 0 <= ny < m:   # 범위를 벗어난 곳으로 이동하는 경우
        continue   # 넘어간다

    # 위치별 값을 저장
    east, west, south, north, up, down = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    # 이동 방향별로 주사위 값 변경
    if d == 1:
        dice[0], dice[1], dice[4], dice[5] = down, up, east, west
    elif d == 2:
        dice[0], dice[1], dice[4], dice[5] = up, down, west, east
    elif d == 3:
        dice[2], dice[3], dice[4], dice[5] = up, down, north, south
    elif d == 4:
        dice[2], dice[3], dice[4], dice[5] = down, up, south, north

    # 도착지 바닥의 숫자 계산
    if maps[nx][ny] == 0:   # 바닥이 0인 경우
        maps[nx][ny] = dice[5]   # 주사위 바닥면 값을 저장
    else:   # 0이 아닌 경우
        dice[5] = maps[nx][ny]   # 주사위 바닥면에 바닥 값 저장
        maps[nx][ny] = 0   # 바닥 값 0으로 초기화

    x, y = nx, ny   # 위치 갱신
    print(dice[4])   # 주사위 윗면 출력

# 오답
# from collections import deque
#
# N, M, y, x, K = map(int, input().split())
# matrix = [list((map(int, input().split()))) for _ in range(N)]
# orders = list(map(int, input().split()))
# ud_dice = deque([0] * 4)   # 2, 1, 5, 6
# lr_dice = deque([0] * 4)   # 4, 1, 3, 6
#
#
# dy = [0, 0, 0, -1, 1]
# dx = [0, 1, -1, 0, 0]
#
# for order in orders:
#
#     ny = y + dy[order]
#     nx = x + dx[order]
#
#     if 0 <= nx < M and 0 <= ny < N:
#         y = ny
#         x = nx
#
#         if order == 1:
#             lr_dice.appendleft(lr_dice.pop())
#             ud_dice[1] = lr_dice[1]
#             ud_dice[3] = lr_dice[3]
#         if order == 2:
#             lr_dice.append(lr_dice.popleft())
#             ud_dice[1] = lr_dice[1]
#             ud_dice[3] = lr_dice[3]
#         if order == 3:
#             ud_dice.append(ud_dice.popleft())
#             lr_dice[1] = ud_dice[1]
#             lr_dice[3] = ud_dice[3]
#         if order == 4:
#             ud_dice.appendleft(ud_dice.pop())
#             lr_dice[1] = ud_dice[1]
#             lr_dice[3] = ud_dice[3]
#
#         if matrix[y][x] == 0:
#             matrix[y][x] == ud_dice[3]
#         else:
#             ud_dice[3] = matrix[y][x]
#             lr_dice[3] = matrix[y][x]
#             matrix[y][x] = 0
#         print(lr_dice[1])
