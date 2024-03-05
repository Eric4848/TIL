import sys
from collections import deque

input = sys.stdin.readline


# 이동 가능 여부 확인
def check(nr, nc, k):
    if 0 <= nr < H and 0 <= nc < W and not answers[k][nr][nc] and maps[nr][nc] == 0:
        return True
    return False


# 이동 bfs
def bfs():
    q = deque([(0, 0, 0)])   # H, W, 말처럼 이동한 횟수
    while q:
        r, c, move = q.popleft()

        # 도착지에 도착한 경우
        if r == H-1 and c == W-1:
            return answers[move][r][c]   # 계산 결과를 반환

        # 평범하게 이동
        for i in range(4):   # 4방향별로
            nr = r + dr[i]
            nc = c + dc[i]
            if check(nr, nc, move):   # 이동 가능하다면
                answers[move][nr][nc] = answers[move][r][c] + 1   # 일반 이동위치에 이전 위치까지 이동횟수 + 1
                q.append((nr, nc, move))   # 큐에 추가

        # 말처럼 이동
        if move < K:   # 말처럼 이동한 횟수가 제한보다 적다면
            for i in range(8):   # 각 방향마다
                nr = r + hr[i]
                nc = c + hc[i]
                if check(nr, nc, move+1):   # 이동할 수 있으면
                    answers[move+1][nr][nc] = answers[move][r][c] + 1   # 말처럼 이동한 위치에 이전 위치까지 이동횟수 + 1
                    q.append((nr, nc, move+1))   # 말처럼 이동한 횟수를 늘려 큐에 추가

    return -1   # 도착할수 없다면 -1 반환


K = int(input())
W, H = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(H)]
answers = [[[0] * W for _ in range(H)] for _ in range(K+1)]   # 이동구역 크기만큼 말처럼 이동 가능 횟수 + 1만큼 만든다(0회의 경우 포함)
# 말처럼 이동
hr = [-1, -2, -2, -1, 1, 2, 2, 1]
hc = [-2, -1, 1, 2, 2, 1, -1, -2]
# 일반 이동
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

print(bfs())


# 시간 초과
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# K = int(input())
# W, H = map(int, input().split())
# maps = [list(map(int, input().split())) for _ in range(H)]
# answers = [[[0] * W for _ in range(H)] for _ in range(K+1)]
# chk = 1
# hr = [-1, -2, -2, -1, 1, 2, 2, 1]
# hc = [-2, -1, 1, 2, 2, 1, -1, -2]
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
#
# q = deque([(0, 0, 0)])
# while q:
#     r, c, move = q.popleft()
#
#     if r == H-1 and c == W-1:
#         print(answers[move][r][c])
#         chk = 0
#         break
#
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < H and 0 <= nc < H and maps[nr][nc] == 0 and not answers[move][nr][nc]:
#             answers[move][nr][nc] = answers[move][r][c] + 1
#             q.append((nr, nc, move))
#
#     if move < K:
#         for i in range(8):
#             nr = r + hr[i]
#             nc = c + hc[i]
#             if 0 <= nr < H and 0 <= nc < H and maps[nr][nc] == 0 and not answers[move][nr][nc]:
#                 answers[move+1][nr][nc] = answers[move][r][c] + 1
#                 q.append((nr, nc, move+1))
#
# if chk:
#     print(-1)


# 오답
# from collections import deque
#
# K = int(input())
# W, H = map(int, input().split())
# maps = [list(map(int, input().split())) for _ in range(H)]
# chk = 1
# hr = [-1, -2, -2, -1, 1, 2, 2, 1]
# hc = [-2, -1, 1, 2, 2, 1, -1, -2]
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
#
# q = deque([(0, 0, K)])
# while q:
#     r, c, left = q.popleft()
#
#     if r == H-1 and c == W-1:
#         print(-maps[r][c])
#         chk = 0
#         break
#
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < H and 0 <= nc < H and maps[nr][nc] == 0:
#             maps[nr][nc] = maps[r][c] - 1
#             q.append((nr, nc, left))
#
#     if 0 < left:
#         for i in range(8):
#             nr = r + hr[i]
#             nc = c + hc[i]
#             if 0 <= nr < H and 0 <= nc < H and maps[nr][nc] == 0:
#                 maps[nr][nc] = maps[r][c] - 1
#                 q.append((nr, nc, left-1))
#
# if chk:
#     print(-1)
