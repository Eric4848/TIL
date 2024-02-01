import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
# 사전 작업
for r in range(n):
    for c in range(m):
        if matrix[r][c] == 1:   # 길이면
            matrix[r][c] = -1   # -1로 변경(도달 불가능한 길인경우)

        elif matrix[r][c] == 2:   # 시작 지점이면
            matrix[r][c] = 0   # 시작 지점을 0으로 초기화
            q = deque([(r, c)])   # deque에 시작 위치 추가

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
# bfs
while q:
    r, c = q.popleft()   # 먼저 추가된 큐부터
    for i in range(4):   # 4방향으로
        nr = r + dr[i]
        nc = c + dc[i]
        # 새로운 위치가 범위 이내고 길이라면
        if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] == -1:
            q.append((nr, nc))   # 해당 위치를 큐에 추가하고
            matrix[nr][nc] += matrix[r][c] + 2   # 해당위치를 이전위치 + 2로 변경

for mat in matrix:
    print(*mat)
