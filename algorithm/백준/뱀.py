import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
matrix = [[0] * N for _ in range(N)]   # N X N 크기의 판
snake = deque()   # 뱀을 담아둘 큐
qc = deque()   # 회전을 담아둘 큐
snake.append((0, 0))   # 뱀을 담아둘 큐에 좌측 상단 위치를 저장한다
answer = 0   # 이동시간을 0으로 초기화 한다

K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    matrix[r-1][c-1] = 1   # 사과가 있는 위치를 1로 표시한다
# 4방향 별로 이동값을 저장한다
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
d = 0   # 처음엔 오른쪽을 보고있으므로 방향을 0번으로 저장한다

L = int(input())
for _ in range(L):
    X, C = input().split()
    X = int(X)
    qc.append((X, C))   # 회전을 담아둘 큐에 회전 시간과 방향을 저장한다

while True:   # 반복문을 돌며
    if qc and answer == qc[0][0]:   # 회전이 남아있고, 회전 시간이 현재 시간이라면
        cd = qc.popleft()   # 회전 리스트에서 popleft한 후
        if cd[1] == 'L':   # 왼쪽이면
            d = (d + 1) % 4   # 좌측으로
        else:   # 아니면
            d = (d - 1) % 4   # 우측으로 이동 방향을 수정한다
    answer += 1   # 시간을 1초 흘려주고
    r, c = snake[-1]   # 현재 위치를 뱀의 위치 맨뒤에서 가져온다
    nr = r + dr[d]   # 다음 위치는
    nc = c + dc[d]   # 현재 위치에 방향을 더해서 구한다
    if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in snake:   # 다음 위치가 판 안에 있고, 뱀의 몸이 아니라면
        snake.append((nr, nc))   # 뱀의 몸에 다음 위치를 추가하고
        if matrix[nr][nc] != 1:   # 그 위치에 사과가 없다면
            snake.popleft()   # 꼬리를 하나 당겨주고
        else:   # 사과가 있다면
            matrix[nr][nc] = 0   # 사과를 먹어준다
    else:   # 판을 넘어가거나 뱀의 몸에 닿은 경우
        print(answer)   # 정답을 출력하고
        break   # 멈춘다


# import sys
# from collections import deque
#
# input = sys.stdin.readline
# N = int(input())
# matrix = [[0] * N for _ in range(N)]
# q = []
# q = deque()
# q.append((0, 0))
# answer = 0
# flag = 1
# K = int(input())
# for _ in range(K):
#     r, c = map(int, input().split())
#     matrix[r-1][c-1] = 1
# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]
# d = 1
#
# L = int(input())
# for _ in range(L):
#     X, C = input().split()
#     X = int(X)
#     if flag:
#         for _ in range(X-answer):
#             answer += 1
#             r, c = q[-1]
#             print(answer)
#             print(r, c)
#             nr = r + dr[d]
#             nc = c + dc[d]
#             if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in q:
#                 print(nr, nc)
#                 print(q)
#                 q.append((nr, nc))
#                 if matrix[nr][nc] == 1:
#                     continue
#                 q.popleft()
#             else:
#                 flag = 0
#                 print(answer)
#                 print('!')
#                 break
#     if C == 'L':
#         d = (d + 1) % 4
#     else:
#         d = (d - 1) % 4
# if flag:
#     print(answer)
