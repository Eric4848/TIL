# Pypy3로 제출
import sys
from collections import deque

input = sys.stdin.readline
H, W = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(H)]
answer = 0
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for y in range(H):
    for x in range(W):
        if maps[y][x] == 'L':   # 육지라면
            tmp = 0   # 임시 계산값 0
            q = deque([(y, x, 0)])   # deque에 현재 위치와 거리 0을 추가
            is_visit = [[False] * W for _ in range(H)]   # 방문여부를 False로 초기화
            is_visit[y][x] = True   # 현재 위치를 방문 처리
            # bfs
            while q:
                r, c, d = q.popleft()
                # 임시 거리 변경
                if tmp < d:
                    tmp = d
                # 다음 방향 계산
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    # 4방향으로 범위 이내, 방문 X, 육지라면 방문처리, 큐에 거리 1 늘려서 추가
                    if 0 <= nr < H and 0 <= nc < W and not is_visit[nr][nc] and maps[nr][nc] == 'L':
                        is_visit[nr][nc] = True
                        q.append((nr, nc, d+1))
            # bfs 후 정답 계산
            answer = max(answer, tmp)

print(answer)


# 시간 초과
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# H, W = map(int, input().split())
# maps = [list(input().rstrip()) for _ in range(H)]
# answer = 0
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
#
# for y in range(H):
#     for x in range(W):
#         if maps[y][x] == 'L':
#             tmp = 0
#             q = deque([(y, x, 0)])
#             is_visit = [[False] * W for _ in range(H)]
#             is_visit[y][x] = True
#             while q:
#                 r, c, d = q.popleft()
#                 if tmp < d:
#                     tmp = d
#
#                 for i in range(4):
#                     nr = r + dr[i]
#                     nc = c + dc[i]
#                     if 0 <= nr < H and 0 <= nc < W and not is_visit[nr][nc] and maps[nr][nc] == 'L':
#                         is_visit[nr][nc] = True
#                         q.append((nr, nc, d+1))
#             answer = max(answer, tmp)
#
# print(answer)
