from collections import deque

N, M = map(int, input().split())
board = [0] * 101   # 게임판을 0으로 초기화(인덱스를 맞추기 위해 101까지)
for _ in range(N+M):
    u, v = map(int, input().split())
    board[u] = v   # 뱀과 사다리의 시점에 도착지점 위치를 저장

q = deque()   # bfs를 진행하기 위한 큐
q.append(1)   # 시작위치인 1을 추가한다

while q:
    now = q.popleft()   # popleft하여 현재 위치 불러오기

    if now == 100:   # 도착지점이면
        print(-board[now])   # 이동 횟수를 양수로 바꿔 출력
        break

    for i in range(1, 7):
        nxt = now + i   # 도착지점을 nxt로 설정

        if 100 < nxt:   # 범위 밖이면
            break   # 뒤는 볼 필요가 없다

        if 0 < board[nxt]:   # 양수가 입력되어있으면(사다리나 뱀이면)
            nxt = board[nxt]   # 도착지점을 탄 후로 변경한다

        if board[nxt] == 0:   # 도착 위치가 0(온 적이 없으면
            board[nxt] = board[now] - 1   # 현재 위치의 숫자 -1을 하여 저장하고
            q.append(nxt)   # 큐에 추가한다
        else:   # 그 외의 경우(-1 이하인 경우)
            pass   # 넘어간다(이미 방문했으므로)
