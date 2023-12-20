import sys

input = sys.stdin.readline
R, C = map(int, input().split())
boards = [input() for _ in range(R)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
q = set([(0, 0, boards[0][0])])   # 큐를 set으로 생성한다(지나온 길이 동일한 경우 제거)
answer = 1   # 정답을 1로 초기화 좌측 상단 알파벳 1개
while q:
    r, c, visits = q.pop()   # 현재 위치와 지나온 알파벳들을 무작위로 하나 뽑는다(set의 특성)
    answer = max(answer, len(visits))   # 정답을 현재와 지나온 알파벳들의 길이 중 큰 것으로 변경한다

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C and boards[nr][nc] not in visits:   # 범위 내 방문하지 않은 알파벳이라면
            q.add((nr, nc, visits + boards[nr][nc]))   # 큐(set)에 추가한다
print(answer)


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# R, C = map(int, input().split())
# boards = [input() for _ in range(R)]
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
# visited = {chr(i+65): 0 for i in range(26)}
# answer = 1
# visited[boards[0][0]] = 1
#
#
# def dfs(r, c, visits):
#     global answer
#
#     if answer < visits:
#         answer = visits
#
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < R and 0 <= nc < C:
#             if not visited[boards[nr][nc]]:
#                 visited[boards[nr][nc]] = 1
#                 dfs(nr, nc, visits+1)
#                 visited[boards[nr][nc]] = 0
#
#
# dfs(0, 0, 1)
# print(answer)


# 시간 초과
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# R, C = map(int, input().split())
# boards = [input() for _ in range(R)]
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
# q = deque([(0, 0, [boards[0][0]])])
# while q:
#     r, c, visits = q.popleft()
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < R and 0 <= nc < C:
#             if boards[nr][nc] not in visits:
#                 q.append((nr, nc, visits + [boards[nr][nc]]))
# print(len(visits))