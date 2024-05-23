import sys
from collections import deque

input = sys.stdin.readline
N, M, T = map(int, input().split())
castles = [list(map(int, input().split())) for _ in range(N)]
times = [[float('inf')] * M for _ in range(N)]   # 무기 없이 걸린 시간 초기화
gtimes = [[float('inf')] * M for _ in range(N)]   # 무기 들고 걸린 시간 초기화
answer = T+1   # 정답을 제한시간 + 1로 초기화
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
q = deque([(0, 0, 0, 0)])   # 시작위치, 걸린시간, 무기 여부 초기화하여 deque에 입력
# bfs
while q:
    r, c, t, grahm = q.popleft()   # 위치, 시간, 무기정보를 가져온다
    # 시간 초과 시 종료
    if t == T+1:
        break
    # 도착 지점 검사
    if r == N-1 and c == M-1:   # 도착 지점이라면
        answer = min(answer, t)   # 정답을 걸린 시간과 비교하여 적은것 저장
    # 이동
    if grahm:   # 무기가 있다면
        for i in range(4):   # 방향별로
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:   # 범위 내인 경우
                if t+1 < gtimes[nr][nc]:   # 무기 들고 걸린 시간보다 현재 이동시간이 짧다면
                    q.append([nr, nc, t+1, 1])   # 큐에 추가
                    gtimes[nr][nc] = t+1   # 시간 변경
    else:   # 무기가 없다면
        for i in range(4):   # 방향별로
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:   # 범위 내인 경우
                if t+1 < times[nr][nc]:   # 무기 없이 걸린시간보다 적은 경우(무기를 줍는다 해도 무기시간으로 계산할 필요 없다)
                    if castles[nr][nc] == 2:   # 무기가 있다면
                        q.append([nr, nc, t+1, 1])   # 큐에 무기를 추가하여 추가
                        gtimes[nr][nc] = t+1   # 무기 든 시간 변경
                    elif castles[nr][nc] == 0:   # 일반 길이라면
                        q.append([nr, nc, t+1, 0])   # 큐에 추가
                        times[nr][nc] = t+1   # 무기 없는 시간 변경

if answer == T+1:   # 시간 내에 불가능하다면
    print('Fail')   # 'Fail' 출력
else:   # 시간 내에 가능하다면
    print(answer)   # 정답 출력
