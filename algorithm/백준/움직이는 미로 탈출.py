from collections import deque

boards = [list(input().rstrip()) for _ in range(8)]   # 체스판 입력
# 8방향 + 제자리
dr = [-1, -1, -1, 0, 1, 1, 1, 0, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1, 0]
q = deque([(7, 0, 0)])   # deque에 시작위치 7, 0 ,지나간 시간 0 추가
# bfs 진행
while q:
    r, c, t = q.popleft()   # 위치, 지난 시간을 가져온다
    if r == 0 and c == 7:   # 목적지에 도착하면
        print(1)   # 1 출력
        exit()   # 종료
    # 이동 계산
    for i in range(9):
        nr = r + dr[i]   # 8방향 + 정지
        nc = c + dc[i]   # 방향별로
        if 0 <= nr < 8 and 0 <= nc < 8:   # 위치가 체스판 이내인 경우
            # 벽인지 확인
            if 0 <= nr - t and boards[nr - t][nc] == '#':   # 내려온 시간만큼 윗칸이 있고, 그곳이 벽이라면
                continue   # 지나간다
            # 벽에 깔리는지 확인
            if 0 <= nr - t - 1 and boards[nr - t - 1][nc] == '#':   # 내려온 시간만큼 윗칸의 윗칸이 있고, 그곳이 벽이라면
                continue   # 지나간다
            q.append((nr, nc, t+1))   # 두 제약에 걸리지 않았다면 다음지역, 시간 + 1을 큐에 추가

print(0)   # bfs가 종료할때까지 도착하지 못하면 0 출력
