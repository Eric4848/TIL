from collections import deque   # bfs 사용


def bfs():
    q = deque()   # 큐를 생성하여
    q.append((s1, s2))   # 시작 위치를 추가한다
    dx = [-1, 1, 2, 2, 1, -1, -2, -2]   # 나이트의 8 이동방향
    dy = [2, 2, 1, -1, -2, -2, -1, 1]
    while q:   # 큐에 도착 가능 위치가 있으면
        x, y = q.popleft()   # 그 위치를 꺼내
        if x == e1 and y == e2:   # 목표 지점이면
            return matrix[x][y]   # 그 지점의 값을 반환한다
        for i in range(8):   # 8방향별로
            nx = x + dx[i]   # 도착 위치를 구하고
            ny = y + dy[i]
            if 0 <= nx < L and 0 <= ny < L and matrix[nx][ny] == 0 :   # 범위 내의 존재하는 가본 적 없는 위치인 경우
                matrix[nx][ny] = matrix[x][y] + 1   # 그 위치에 출발 위치까지 이동횟수 + 1을 저장하고
                q.append((nx, ny))   # 큐에 추가한다


T = int(input())
for _ in range(T):
    answer = 0
    L = int(input())
    matrix = [[0] * L for _ in range(L)]   # 모든 위치를 0으로 초기화(처음 위치도 이동 횟수가 0)
    s1, s2 = map(int, input().split())
    e1, e2 = map(int, input().split())
    print(bfs())
