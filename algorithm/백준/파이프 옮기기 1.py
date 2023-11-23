import sys

home = []
N = int(input())
for _ in range(N):
    home.append([int(x) for x in sys.stdin.readline().rstrip().split()])

DP = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]   # 0 가로, 1 세로, 2 대각선 순으로 리스트를 0으로 초기화 해 만든다

DP[0][0][1] = 1   # 첫번째 가로로 놓는 경우 1로 변경한다
# 맨 윗줄 계산
for i in range(2, N):   # 가로방향으로
    if home[0][i] == 0:   # 다음 위치가 벽이 아니라면
        DP[0][0][i] = DP[0][0][i - 1]   # 이전 값을 이어받는다


for i in range(1, N):   # 가로
    for j in range(1, N):   # 세로
        # 대각선
        if home[i][j] == 0 and home[i][j - 1] == 0 and home[i - 1][j] == 0:   # 대각선, 가로, 아래가 전부 벽이 아니라면
            DP[2][i][j] = DP[0][i - 1][j - 1] + DP[1][i - 1][j - 1] + DP[2][i - 1][j - 1]   # 세 방향별로 놓을수 있는 수를 더해 대각선에 저장한다

        if home[i][j] == 0:   # 어떤 지점에 벽이 없다면
            # 가로
            DP[0][i][j] = DP[0][i][j - 1] + DP[2][i][j - 1]   # 가로방향 이전 칸의 가능한 수와 대각선 방향 이전 칸의 가능한 수를 더해 저장한다
            # 세로
            DP[1][i][j] = DP[1][i - 1][j] + DP[2][i - 1][j]   # 가로의 경우와 동일
print(DP[0][N - 1][N - 1] + DP[1][N - 1][N - 1] + DP[2][N - 1][N - 1])   # 세 방향별 이동 가능 횟수를 더해 출력한다


# 시간초과(63%)
# N = int(input())
# house = [list(map(int, input().split())) for _ in range(N)]
# answer = [0]
# dr = [0, 1, 1]
# dc = [1, 0, 1]
#
#
# def move(r, c, s):
#     if r == c == N-1:
#         answer[0] += 1
#         return
#
#     for i in range(3):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if nr == N or nc == N or house[nr][nc] == 1:
#             break
#         if i == 2:
#             move(r+1, c+1, 2)
#
#     if s == 2:
#         for i in range(2):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if nr < N and nc < N and not house[nr][nc]:
#                 move(nr, nc, i)
#
#     else:
#         nr = r + dr[s]
#         nc = c + dc[s]
#         if nr < N and nc < N and not house[nr][nc]:
#             move(nr, nc, s)
#
#
# move(0, 1, 0)
# print(answer[0])


# 시간초과(40%)
# from collections import deque
#
# N = int(input())
# house = [list(map(int, input().split())) for _ in range(N)]
# answer = [0]
# dr = [0, 1, 1]
# dc = [1, 0, 1]
# q = deque()
# q.append([0, 1, 0])
#
#
# while q:
#     r, c, s = q.popleft()
#     if r == c == N-1:
#         answer[0] += 1
#         continue
#
#     chk = 1
#     for i in range(3):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if nr == N or nc == N or house[nr][nc] == 1:
#             chk = 0
#
#     if chk:
#         q.append([r+1, c+1, 2])
#
#     if s == 2:
#         for i in range(2):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if nr < N and nc < N and not house[nr][nc]:
#                 q.append([nr, nc, i])
#
#     else:
#         nr = r + dr[s]
#         nc = c + dc[s]
#         if nr < N and nc < N and not house[nr][nc]:
#             q.append([nr, nc, s])
#
#
# print(answer[0])


# 시간 초과(60%)
# N = int(input())
# house = [list(map(int, input().split())) for _ in range(N)]
# answer = [0]
# dr = [0, 1, 1]
# dc = [1, 0, 1]
#
#
# def move(r, c, s):
#     if r == c == N-1:
#         answer[0] += 1
#         return
#
#     chk = 1
#     for i in range(3):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if nr == N or nc == N or house[nr][nc] == 1:
#             chk = 0
#
#     if chk:
#         move(r+1, c+1, 2)
#
#     if s == 2:
#         for i in range(2):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if nr < N and nc < N and not house[nr][nc]:
#                 move(nr, nc, i)
#
#     else:
#         nr = r + dr[s]
#         nc = c + dc[s]
#         if nr < N and nc < N and not house[nr][nc]:
#             move(nr, nc, s)
#
#
# move(0, 1, 0)
# print(answer[0])
