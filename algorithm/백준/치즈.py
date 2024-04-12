import sys
from collections import deque

input = sys.stdin.readline
R, C = map(int, input().split())
cheezes = [list(map(int, input().split())) for _ in range(R)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
time = 0   # 시간 초기화
melts = []   # 녹인 치즈 갯수를 담을 리스트

# 시간을 지나가게 함
while True:
    is_visit = [[0 for _ in range(C)] for _ in range(R)]   # 방문 여부 초기화
    q = deque([(0, 0)])  # 계산할 위치를 좌측 상단으로 설정(판의 위치 중 하나)
    melt = 0  # 녹은 치즈 갯수 초기화
    while q:  # bfs계산
        r, c = q.popleft()   # 위치를 가져와서
        for i in range(4):   # 4방향별로
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and not is_visit[nr][nc]:   # 범위 내 방문한 적 없는 위치라면
                is_visit[nr][nc] = 1   # 방문처리
                if cheezes[nr][nc] == 0:   # 공기라면
                    q.append((nr, nc))   # 큐에 추가
                else:   # 치즈라면 큐에 추가하지 않음 -> 주변 확인하지 않기 때문에 치즈의 구멍, 녹음 처리한 것에 영향을 주지 않음
                    cheezes[nr][nc] = 0   # 녹음 처리
                    melt += 1   # 녹은 갯수 + 1
    if melt == 0:   # 녹은 치즈가 없다면
        break   # 종료
    time += 1   # 시간 + 1
    melts.append(melt)   # 녹인 갯수에 이번 시간에 녹인 갯수 추가

print(time)   # 소요된 시간 출력
print(melts[-1])   # 마지막으로 녹인 갯수 출력
