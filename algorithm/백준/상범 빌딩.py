import sys
from collections import deque

input = sys.stdin.readline
dl = [1, -1, 0, 0, 0, 0]
dr = [0, 0, 1, -1, 0, 0]
dc = [0, 0, 0, 0, 1, -1]
while True:
    L, R, C = map(int, input().split())
    # 종료 조건에 맞으면 종료
    if L == R == C == 0:
        break

    buildings = []   # 건물 리스트 초기화
    able = 0   # 탈출 가능여부 초기화

    for _ in range(L):   # 층별로
        buildings.append([list(input().strip()) for _ in range(R)])   # 면을 건물에 추가하고
        blank = input()   # 빈 곳을 빼준다
    # 전체를 돌며 시작지점 찾기
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if buildings[i][j][k] == 'S':
                    q = deque([(i, j, k)])   # deque에 시작지점 추가
                    buildings[i][j][k] = 0   # 시작지점을 0분으로 초기화

    while q:   # 큐가 있는 동안
        if able:   # 도착했다면
            break   # 종료

        l, r, c = q.popleft()
        for i in range(6):   # 6방향별로
            nl = l + dl[i]
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C:   # 범위 이내라면
                if buildings[nl][nr][nc] == '.':   # 갈 수 있는 길이면
                    q.append((nl, nr, nc))   # 큐에 추가하고
                    buildings[nl][nr][nc] = buildings[l][r][c] + 1   # 해당 지점을 이전 시간 + 1분으로 설정
                elif buildings[nl][nr][nc] == 'E':   # 도착 지점이면
                    print(f'Escaped in {buildings[l][r][c] + 1} minute(s).')   # 시간을 출력하고
                    able = 1   # 도달할 수 있다고 변경

    if not able:   # 갈 수 없다면
        print('Trapped!')   # 없다고 출력


# import sys
# from collections import deque
#
# input = sys.stdin.readline
# dl = [1, -1, 0, 0, 0, 0]
# dr = [0, 0, 1, -1, 0, 0]
# dc = [0, 0, 0, 0, 1, -1]
# while True:
#     L, R, C = map(int, input().split())
#
#     if L == R == C == 0:
#         break
#
#     buildings = []
#     visits = [[[0] * C for _ in range(R)] for _ in range(L)]   # 방문
#     chk = 1
#
#     for _ in range(L):
#         buildings.append([list(input().strip()) for _ in range(R)])
#         blank = input()
#
#     for i in range(L):
#         for j in range(R):
#             for k in range(C):
#                 if buildings[i][j][k] == 'S':
#                     q = deque([(i, j, k)])
#
#     while q:
#         if not chk:
#             break
#
#         l, r, c = q.popleft()
#         for i in range(6):
#             nl = l + dl[i]
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C:
#                 if buildings[nl][nr][nc] == '.' and not visits[nl][nr][nc]:
#                     q.append((nl, nr, nc))
#                     visits[nl][nr][nc] = visits[l][r][c] + 1
#                 elif buildings[nl][nr][nc] == 'E':
#                     print(f'Escaped in {visits[l][r][c] + 1} minute(s).')
#                     chk = 0
#
#     if chk:
#         print('Trapped!')


# 시간 초과
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# dl = [1, -1, 0, 0, 0, 0]
# dr = [0, 0, 1, -1, 0, 0]
# dc = [0, 0, 0, 0, 1, -1]
# while True:
#     L, R, C = map(int, input().split())
#     if L == R == C == 0:
#         break
#
#     buildings = []
#     visits = [[[0] * C for _ in range(R)] for _ in range(L)]
#     chk = 1
#
#     for _ in range(L):
#         buildings.append([list(input().strip()) for _ in range(R)])
#         blank = input()
#
#     for i in range(L):
#         for j in range(R):
#             for k in range(C):
#                 if buildings[i][j][k] == 'S':
#                     q = deque([(i, j, k)])
#
#     while q:
#         if not chk:
#             break
#
#         l, r, c = q.popleft()
#         for i in range(6):
#             nl = l + dl[i]
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C:
#                 if buildings[nl][nr][nc] == '.':
#                     q.append((nl, nr, nc))
#                     visits[nl][nr][nc] = visits[l][r][c] + 1
#                 elif buildings[nl][nr][nc] == 'E':
#                     print(f'Escaped in {visits[l][r][c] + 1} minute(s).')
#                     chk = 0
#
#     if chk:
#         print('Trapped!')
