from collections import deque

dr = [1, -1, 0, 0]   # 행이동
dc = [0, 0, 1, -1]   # 열이동

N, M = map(int, input().split())
mat = [list(map(int, input())) for _ in range(M)]   # 미로 입력받음
crash = [[-1] * N for _ in range(M)]   # 벽을 부순 횟수를 -1로 초기화

q = deque()   # 벽이 없는 경우 우선 선택을 위해 deque 사용
q.append((0, 0))   # 큐에 시작위치 저장
crash[0][0] = 0   # 시작 위치에 벽돌 부순 횟수를 0으로 초기화
while q:
    r, c = q.popleft()
    # 도착지점에 도달한지 확인하지 않는것이 더 빠르다
    # if r == M - 1 and N == N - 1:
    #     break

    for k in range(4):   # 4방향으로
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < M and 0 <= nc < N:   # 미로 내 영역이면
            if crash[nr][nc] == -1:   # 가본 적 없는 곳인 경우
                if mat[nr][nc] == 0:   # 벽이 없으면
                    crash[nr][nc] = crash[r][c]   # 그 위치에 이전까지 벽돌 부순 횟수를 저장
                    q.appendleft((nr, nc))   # 그 위치를 appendleft로 먼저 확인
                else:   # 벽이 있으면
                    crash[nr][nc] = crash[r][c] + 1   # 그 위치에 이전까지 벽돌 부순 횟수 + 1을 저장
                    q.append((nr, nc))   # 그 위치를 append로 나중에 확인
print(crash[M - 1][N - 1])   # 도착지점의 벽돌 부순 횟수 출력


# 메모리 초과
# import sys
#
# sys.setrecursionlimit(10 ** 9)
# N, M = map(int, input().split())
# mat = [list(map(int, input().rstrip())) for _ in range(M)]
# answer = [N + M]
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
#
#
# def move(r, c, crash):
#     if answer[0] < crash:
#         return
#
#     if r == M-1 and c == N-1:
#         answer[0] = min(answer[0], crash)
#         return
#
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < M and 0 <= nc < N:
#             if mat[nr][nc] == 1:
#                 move(nr, nc, crash+1)
#             else:
#                 move(nr, nc, crash)
#
#
# move(0, 0, 0)
# print(answer[0])


# 시간 초과
# import sys
#
# sys.setrecursionlimit(10 ** 9)
# N, M = map(int, input().split())
# mat = [list(map(int, input().rstrip())) for _ in range(M)]
# answer = [N + M]
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
# is_visit = [[False] * N for _ in range(M)]
# is_visit[0][0] = True
#
#
# def move(r, c, crash):
#     if answer[0] <= crash:
#         return
#
#     if r == M-1 and c == N-1:
#         answer[0] = min(answer[0], crash)
#         return
#
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < M and 0 <= nc < N and not is_visit[nr][nc]:
#             is_visit[nr][nc] = True
#             if mat[nr][nc] == 1:
#                 move(nr, nc, crash+1)
#             else:
#                 move(nr, nc, crash)
#             is_visit[nr][nc] = False
#
#
# move(0, 0, 0)
# print(answer[0])


# 시간 초과
# import copy
# import sys
#
# sys.setrecursionlimit(10 ** 9)
# N, M = map(int, input().split())
# mat = [list(map(int, input().rstrip())) for _ in range(M)]
# answer = [N + M]
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
# is_visit = [[False] * N for _ in range(M)]
# is_visit[0][0] = True
#
#
# def move(r, c, crash, visit):
#     if answer[0] < crash:
#         return
#
#     if r == M-1 and c == N-1:
#         answer[0] = min(answer[0], crash)
#         return
#
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < M and 0 <= nc < N and not visit[nr][nc]:
#             tmp = copy.deepcopy(visit)
#             tmp[nr][nc] = True
#             if mat[nr][nc] == 1:
#                 move(nr, nc, crash+1, tmp)
#             else:
#                 move(nr, nc, crash, tmp)
#
#
# move(0, 0, 0, is_visit)
# print(answer[0])
