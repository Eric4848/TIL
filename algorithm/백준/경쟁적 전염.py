import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
tests = [list(map(int, input().split())) for _ in range(N)]
virus = [deque([]) for _ in range(K+1)]   # 종류별 바이러스들의 위치를 담을 리스트를 deque로 만든다
S, X, Y = map(int, input().split())

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

# 바이러스 위치 저장
for r in range(N):
    for c in range(N):
        if tests[r][c]:   # 바이러스가 있으면
            virus[tests[r][c]].append((r, c))   # 바이러스 번호의 리스트에 위치를 저장한다

# 바이러스 증식
for _ in range(S):   # 제시된 횟수만큼
    for i in range(1, K+1):   # 바이러스의 종류 번호가 낮은 순으로
        for _ in range(len(virus[i])):   # 현재 저장되어있는 바이러스 수만큼(같은 리스트에 추가할 예정)
            r, c = virus[i].popleft()   # popleft하여 위치를 불러온다
            for j in range(4):   # 4방향으로
                nr = r + dr[j]
                nc = c + dc[j]
                if 0 <= nr < N and 0 <= nc < N and not tests[nr][nc]:   # 범위 이내이며 해당 위치에 바이러스가 없다면
                    tests[nr][nc] = i   # 현재 바이러스로 증식시키고
                    virus[i].append((nr, nc))   # 바이러스 위치에 추가해준다

print(tests[X-1][Y-1])


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# N, K = map(int, input().split())
# tests = [list(map(int, input().split())) for _ in range(N)]
# virus = [[] for _ in range(K+1)]
# is_visit = [[False] * N for _ in range(N)]
# S, X, Y = map(int, input().split())
#
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
#
# for _ in range(S):
#     for r in range(N):
#         for c in range(N):
#             if tests[r][c] and not is_visit[r][c]:
#                 virus[tests[r][c]].append((r, c))
#                 is_visit[r][c] = True
#
#     for i in range(1, K+1):
#         while virus[i]:
#             r, c = virus[i].pop()
#             for j in range(4):
#                 nr = r + dr[j]
#                 nc = c + dc[j]
#                 if 0 <= nr < N and 0 <= nc < N and not tests[nr][nc]:
#                     tests[nr][nc] = i
#
# print(tests[X-1][Y-1])
