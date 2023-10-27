from collections import deque

R, C = map(int, input().split())
maps = [input().strip() for _ in range(R)]
waters = deque()   # 물의 위치를 저장할 리스트
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
is_visit = [[False] * C for _ in range(R)]   # 도망쳐온 길인지 저장할 리스트를 False로 초기화
flag = 1   # 탈출할수 없는지 표시

for r in range(R):
    for c in range(C):   # 모든 위치별로
        if maps[r][c] == 'D':   # 도착지면
            D = (r, c)   # 도착지 위치를 저장
        elif maps[r][c] == 'S':   # 출발지면
            S = (r, c, 0)   # 출발지 위치를 걸린 시간 0과 함께 저장
            is_visit[r][c] = True   # 출발지를 방문처리
        elif maps[r][c] == '*':   # 물이 있으면
            waters.append((r, c))   # 물 리스트에 추가

q = deque()   # deque를 선언
q.append(S)   # 큐에 출발지를 추가

while q:   # 출발지가 있는 경우
    # 물 흘러들어감
    for _ in range(len(waters)):
        wr, wc = waters.popleft()   # 각 물들의 위치마다
        for j in range(4):    # 4방향으로
            nr = wr + dr[j]
            nc = wc + dc[j]
            if 0 <= nr < R and 0 <= nc < C:   # 범위 안이고
                if maps[nr][nc] == '.':   # 도망칠 길이라면
                    maps[nr] = maps[nr][:nc] + '*' + maps[nr][nc + 1:]   # 도망칠 길을 '*'로 바꿔준 후
                    waters.append((nr, nc))   # 물 리스트에 추가

    for _ in range(len(q)):   # 큐의 갯수만큼 (같은 날)
        sr, sc, times = q.popleft()   # 현재 r, 현재 c, 걸린 일수
        if (sr, sc) == D:   # 집으로 탈출 한 경우
            print(times)   # 걸린 시간을 출력하고
            flag = 0   # 탈출할 수 있음으로 변경하고
            break   # 종료한다

        for i in range(4):   # 4방향별로
            nr = sr + dr[i]
            nc = sc + dc[i]
            if 0 <= nr < R and 0 <= nc < C:   # 범위 내이고
                if maps[nr][nc] != 'X' and maps[nr][nc] != '*':   # 돌이나 물로 막히지 않은 경우
                    if not is_visit[nr][nc]:   # 해당 위치를 방문하지 않았다면
                        q.append((nr, nc, times+1))   # 큐에 해당 위치를 걸린 시간에 1 추가하여 저장
                        is_visit[nr][nc] = True   # 해당위치를 방문처리

if flag:   # 탈출 불가능하면
    print('KAKTUS')   # 'KAKTUS'를 출력
