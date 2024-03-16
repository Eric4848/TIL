import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

# 섬 별로 구분
cnt = 0   # 추가할 섬 번호를 0으로 초기화
is_visit = [[False for _ in range(N)] for _ in range(N)]   # 방문 리스트 초기화
for y in range(N):
    for x in range(N):
        if maps[y][x] == 1:   # 섬이라면
            cnt += 1   # 섬번호를 1 증가
            q = deque([(y, x)])   # deque에 현 위치 추가
            is_visit[y][x] = True   # 현 위치 방문처리
            # 붙어있는 섬을 찾는 bfs
            while q:
                r, c = q.popleft()
                maps[r][c] += cnt   # 현위치에 섬번호 추가
                for i in range(4):   # 4방향으로
                    nr = r + dr[i]
                    nc = c + dc[i]
                    # 범위 이내, 방문하지 않은 섬이면
                    if 0 <= nr < N and 0 <= nc < N and not is_visit[nr][nc] and maps[nr][nc] == 1:
                        q.append((nr, nc))   # 큐에 추가
                        is_visit[nr][nc] = True   # 방문 처리

# 최소거리 계산
answer = float('inf')   # 정답을 무한으로 초기화
for r in range(N):
    for c in range(N):
        if maps[r][c] != 0:   # 섬이라면
            start = maps[r][c]   # 시작 섬 번호 저장
            q = deque([(r, c, -1)])   # deque에 섬위치와 거리 -1 저장(두 지점 사이의 거리이므로)
            is_visit = [[False for _ in range(N)] for _ in range(N)]   # 방문 리스트 초기화
            is_visit[r][c] = True   # 시작위치 방문처리
            # 다른 섬을 찾는 bfs
            while q:
                R, C, D = q.popleft()

                # 정답보다 거리가 멀다면 종료
                if answer < D:
                    break

                # 도착한 곳이 다른 섬이면 정답과 거리 중 작은 것 저장
                if maps[R][C] != 0 and maps[R][C] != start:
                    answer = min(answer, D)
                    break

                # 다음 방향 계산
                for i in range(4):   # 4방향으로
                    NR = R + dr[i]
                    NC = C + dc[i]
                    # 범위 이내, 방문하지 않은 시작 섬과 다른 지점이면
                    if 0 <= NR < N and 0 <= NC < N and not is_visit[NR][NC] and maps[NR][NC] != start:
                        q.append((NR, NC, D+1))   # 큐에 거리를 1늘려 해당 위치 추가
                        is_visit[NR][NC] = True   # 해당위치 방문처리

print(answer)


# 메모리 초과
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# N = int(input())
# maps = [list(map(int, input().split())) for _ in range(N)]
# is_visit = [[False for _ in range(N)] for _ in range(N)]
# answer = float('inf')
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
#
# cnt = 0
# for y in range(N):
#     for x in range(N):
#         if maps[y][x] == 1:
#             cnt += 1
#             q = deque([(y, x)])
#             is_visit[y][x] = True
#             while q:
#                 r, c = q.popleft()
#                 maps[r][c] += cnt
#                 for i in range(4):
#                     nr = r + dr[i]
#                     nc = c + dc[i]
#                     if 0 <= nr < N and 0 <= nc < N and not is_visit[nr][nc] and maps[nr][nc] == 1:
#                         q.append((nr, nc))
#                         is_visit[nr][nc] = True
#
# for r in range(N):
#     for c in range(N):
#         if maps[r][c] != 0:
#             start = maps[r][c]
#             q = deque([(r, c, -1)])
#             while q:
#                 R, C, D = q.popleft()
#
#                 if answer < D:
#                     break
#
#                 if maps[R][C] != 0 and maps[R][C] != start:
#                     answer = min(answer, D)
#                     break
#
#                 for i in range(4):
#                     NR = R + dr[i]
#                     NC = C + dc[i]
#                     if 0 <= NR < N and 0 <= NC < N and maps[NR][NC] != start:
#                         q.append((NR, NC, D+1))
#
# print(answer)
