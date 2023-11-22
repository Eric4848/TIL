# 시간초과(63%)
N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
answer = [0]
dr = [0, 1, 1]
dc = [1, 0, 1]


def move(r, c, s):
    if r == c == N-1:
        answer[0] += 1
        return

    for i in range(3):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr == N or nc == N or house[nr][nc] == 1:
            break
        if i == 2:
            move(r+1, c+1, 2)

    if s == 2:
        for i in range(2):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < N and nc < N and not house[nr][nc]:
                move(nr, nc, i)

    else:
        nr = r + dr[s]
        nc = c + dc[s]
        if nr < N and nc < N and not house[nr][nc]:
            move(nr, nc, s)


move(0, 1, 0)
print(answer[0])


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
