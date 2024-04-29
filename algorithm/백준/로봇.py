import sys
from collections import deque

input = sys.stdin.readline
M, N = map(int, input().split())
fields = [list(map(int, input().split())) for _ in range(M)]   # 공장 지도
sr, sc, sd = map(int, input().split())   # 시작 위치, 방향
er, ec, ed = map(int, input().split())   # 도착 위치, 방향
# 동, 서, 남, 북 방향
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

# 현재 방향에서 90도 돌린 방향
turn = [(2, 3), (2, 3), (0, 1), (0, 1)]

is_visit = [[[False] * 4 for _ in range(N)] for _ in range(M)]   # 방향별로, 공장 방문 정보를 0으로 초기화
is_visit[sr-1][sc-1][sd-1] = True   # 시작 위치, 방향 방문 처리
q = deque([(sr-1, sc-1, sd-1, 0)])   # 큐에 시작 위치, 방향, 명령 횟수 0 저장
# bfs
while q:
    r, c, d, cnt = q.popleft()   # 큐에서 위치, 방향, 명령 횟수를 가져온다
    # 도착 확인
    if (r, c, d) == (er-1, ec-1, ed-1):   # 위치와 방향이 도착값과 같다면
        print(cnt)   # 명령 횟수를 출력
        break   # 종료

    # 이동 명령
    for dist in range(1, 4):   # 1~3 만큼
        nr = r + dr[d] * dist   # 현재 방향으로
        nc = c + dc[d] * dist   # 이동
        # 종료 조건(더이상 계산 불가)
        if not (0 <= nr < M and 0 <= nc < N) or fields[nr][nc]:
            break

        # 계산 넘어갈 조건
        if is_visit[nr][nc][d]:   # 이미 방문했다면
            continue   # 넘어간다

        q.append((nr, nc, d, cnt + 1))   # 큐에 이동한 거리, 방향, 명령 횟수 + 1 저장
        is_visit[nr][nc][d] = True   # 도착지점 방문 처리

    # 회전 명령
    for nd in turn[d]:   # 회전 가능한 방향별로
        if is_visit[r][c][nd]:   # 해당 방향이 방문했다면
            continue   # 넘어간다
        q.append((r, c, nd, cnt + 1))   # 큐에 위치, 새로운 방향, 명령 횟수 + 1 저장
        is_visit[r][c][nd] = True   # 해당 방향 방문 처리

