import sys
from collections import deque

input = sys.stdin.readline
N, M, K = map(int, input().split())
floors = [[False] * M for _ in range(N)]   # 바닥에 음식물이 없다고 초기화
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
answer = 0   # 정답을 0으로 초기화

# 음식물 정보 추가
for _ in range(K):
    r, c = map(int, input().split())
    floors[r-1][c-1] = True

for R in range(N):
    for C in range(M):
        if floors[R][C]:   # 음식물이 있다면
            q = deque([(R, C)])   # deque를 만들어 위치 추가
            size = 1   # 음식물 크기를 1로 초기화
            floors[R][C] = False   # 위치에 음식물이 없다고 변경
            # bfs로 크기 계산
            while q:
                r, c = q.popleft()   # 현재위치 기준
                for i in range(4):   # 4방면으로
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < N and 0 <= nc < M and floors[nr][nc]:   # 범위 이내이며 음식물이 있다면
                        size += 1   # 크기를 1 늘려주고
                        floors[nr][nc] = False   # 음식물이 없다고 변경
                        q.append((nr, nc))   # 위치를 큐에 추가
            answer = max(answer, size)   # bfs종료 후 정답과 현재 크기중 큰 것 저장

print(answer)
