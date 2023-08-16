from collections import deque   # bfs를 사용하기 위해 deque를 추가

F, S, G, U, D = map(int, input().split())
floors = [-1] * F   # 각 층별 도달 여부를 -1(가지 못함)로 초기화한다
chk = 0   # 목표 층에 도달 가능여부를 0(불가)으로 초기화 한다
floors[S-1] = 0   # 현재층의 도달하는데 까지 걸린 횟수를 0으로 설정한다
queue = deque([S-1])   # 큐에 현재 층을 추가한다
while queue:
    now = queue.popleft()   # 큐의 층을 좌측부터
    if now == G - 1:   # 해당 층이 목표층이면
        print(floors[now])   # 걸린 횟수를 출력하고
        chk = 1   # 도달 가능하다고 변경하고
        break   # 중단한다
    down = now - D   # 아래층 버튼을 누른 경우
    up = now + U   # 위층 버튼을 누른 경우
    if 0 <= down and floors[down] == -1:   # 아래층으로 갈수 있고, 그 층에 가본 적 없는 경우
        queue.append(down)   # 큐에 아래층을 추가하고
        floors[down] = floors[now] + 1   # 아래층까지 도달하는데 걸린 횟수를 이전층 + 1로 저장한다
    if up < F and floors[up] == -1:   # 아래층과 반대
        queue.append(up)
        floors[up] = floors[now] + 1
if chk == 0:
    print("use the stairs")
