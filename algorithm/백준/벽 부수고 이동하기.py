import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
maps = [list(map(int, input().rstrip())) for _ in range(N)]
visits = [[[0] * 2 for _ in range(M)] for _ in range(N)]   # 벽을 안부순 경우, 부순경우의 방문 여부 리스트
visits[0][0][0] = 1   # 벽을 부수지 않은 출발지점을 1로 변경(시작부터 시간 계산)
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
flag = 1   # 도달 불가능한지
q = []
q = deque([(0, 0, 0)])

while q:
    r, c, crash = q.popleft()   # 현재 위치, 벽을 부순 지 여부

    if r == N-1 and c == M-1:   # 도착지점이면
        print(visits[r][c][crash])   # 걸린 시간 출력
        flag = 0   # 도달 가능처리
        break

    for i in range(4):   # 4방향으로
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and visits[nr][nc][crash] == 0:   # 범위 이내이면서 방문하지 않았으면(벽 부순경우, 않은 경우)
            if maps[nr][nc] == 0:   # 해당 위치에 벽이 없으면
                q.append((nr, nc, crash))   # 해당 위치, 벽을 부순 지 여부 저장
                visits[nr][nc][crash] = visits[r][c][crash] + 1   # 해당 위치까지 걸린 시간을 이전위치 + 1로 변경

            elif crash == 0:   # 벽이 있고, 벽을 부순적이 없다면
                q.append((nr, nc, 1))   # 해당 위치, 벽을 부쉈다고 저장
                visits[nr][nc][1] = visits[r][c][0] + 1   # 해당위치까지 걸린 시간을 이전위치 + 1로 변경

if flag:
    print(-1)

# 메모리 초과
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# maps = [list(map(int, input().rstrip())) for _ in range(N)]
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
# flag = 1
# q = []
# q = deque()
# q.append((0, 0, 0, 1))
# while q:
#     r, c, crash, move = q.popleft()
#
#     if crash == 2:
#         continue
#
#     if r == N-1 and c == M-1:
#         print(move)
#         flag = 0
#         break
#
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < N and 0 <= nc < M:
#             wall = maps[nr][nc]
#             q.append((nr, nc, crash+wall, move+1))
# if flag:
#     print(-1)
