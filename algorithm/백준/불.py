import sys
from collections import deque

input = sys.stdin.readline
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    buildings = [list(input().rstrip()) for _ in range(h)]
    f_map = [[0 for _ in range(w)] for _ in range(h)]   # 불의 진행 상황을 초기화
    s_map = [[0 for _ in range(w)] for _ in range(h)]   # 상근이의 진행 상황을 초기화
    qf = deque()   # 불 위치를 담을 deque
    answer = 0   # 정답 초기화

    # 위치별 설정
    for r in range(h):
        for c in range(w):
            # 상근이의 위치
            if buildings[r][c] == '@':
                qs = deque([(r, c)])   # 상근이의 위치 deque생성
                s_map[r][c] = 1   # 상근이의 진행상황의 해당 위치를 1로 변경
                f_map[r][c] = -1   # 불의 진행상황의 해당 위치를 -1로 변경

            # 불의 위치
            elif buildings[r][c] == '*':
                qf.append((r, c))   # 불 위치 큐에 추가
                f_map[r][c] = 1   # 불의 진행상황의 해당 위치를 1로 변경

            # 길인 경우 두 진행상황 모두 해당 위치를 -1로 변경
            elif buildings[r][c] == '.':
                f_map[r][c] = -1
                s_map[r][c] = -1

    # 불 이동
    while qf:
        r, c = qf.popleft()
        # 4방향 별로
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위 이내, 이동 가능한 곳이면
            if 0 <= nr < h and 0 <= nc < w and f_map[nr][nc] == -1:
                f_map[nr][nc] = f_map[r][c] + 1   # 해당 위치를 시작 위치까지 거리 + 1로 변경
                qf.append((nr, nc))   # 불 위치 큐에 추가

    # 상근이 이동
    while qs:
        # 탈출 가능하다면 종료
        if answer:
            break

        # 4방향 별로
        r, c = qs.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위 이내라면
            if 0 <= nr < h and 0 <= nc < w:
                # 상근이가 이동 가능한 위치이고, 불이 이동할 수 있는 곳이거나, 불이 이동하는데 걸리는 시간이 1보다 더 크다면(불이 이동할 위치로 이동 불가)
                if s_map[nr][nc] == -1 and (f_map[nr][nc] == -1 or s_map[r][c] + 1 < f_map[nr][nc]):
                    s_map[nr][nc] = s_map[r][c] + 1   # 해당 위치를 시작 위치까지 거리 + 1로 변경
                    qs.append((nr, nc))   # 상근이 이동 큐에 추가
            # 범위 밖으로 탈출했다면
            else:
                answer = s_map[r][c]   # 정답을 이전 위치로 설정(시작을 1로 했으므로)
                break

    if answer:
        print(answer)
    else:
        print('IMPOSSIBLE')


# 메모리 초과
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
#
#
# def move(d):
#     while qs:
#         d += 1
#         lf = len(qf)
#         for _ in range(lf):
#             r, c = qf.popleft()
#             for i in range(4):
#                 nr = r + dr[i]
#                 nc = c + dc[i]
#                 if 0 <= nr < h and 0 <= nc < w and buildings[nr][nc] == '.':
#                     buildings[nr][nc] = '*'
#                     qf.append((nr, nc))
#
#         ls = len(qs)
#         for _ in range(ls):
#             r, c = qs.popleft()
#             for i in range(4):
#                 nr = r + dr[i]
#                 nc = c + dc[i]
#                 if nr < 0 or h <= nr or nc < 0 or w <= nc:
#                     return d
#
#                 elif 0 <= nr < h and 0 <= nc < w and buildings[nr][nc] == '.':
#                     qs.append((nr, nc))
#
#
# T = int(input())
# for _ in range(T):
#     w, h = map(int, input().split())
#     buildings = [list(input().rstrip()) for _ in range(h)]
#     qf = deque()
#     for r in range(h):
#         for c in range(w):
#             if buildings[r][c] == '@':
#                 qs = deque([(r, c)])
#                 buildings[r][c] = '.'
#
#             elif buildings[r][c] == '*':
#                 qf.append((r, c))
#
#     answer = move(0)
#     if not answer:
#         print('IMPOSSIBLE')
#     else:
#         print(answer)
