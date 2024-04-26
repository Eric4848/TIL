import sys
import heapq


# 4방향으로 쭉 이동시키는 함수
def calc(cnt, r, c):
    for i in range(4):   # 4방향으로
        nr = r + dr[i]   # 다음위치
        nc = c + dc[i]   # 계산
        while True:
            if 0 <= nr < H and 0 <= nc < W:   # 다음 위치가 범위 이내인 경우
                if grounds[nr][nc] == '.':   # 그 위치가 이동 가능한 곳이면
                    # 거울의 갯수가 현 갯수보다 적거나, 갯수가 같고 이동하던 방향이 온 적 없는 경우
                    if cnt < cnts[nr][nc] or (cnt == cnts[nr][nc] and not is_visits[i // 2][nr][nc]):
                        cnts[nr][nc] = cnt   # 해당 위치까지 거울 갯수 갱신
                        is_visits[i // 2][nr][nc] = True   # 해당 위치 이동방향 이동처리
                        heapq.heappush(q, (cnt, nr, nc))   # 큐에 추가
                        nr += dr[i]   # 한칸 더
                        nc += dc[i]   # 이동
                    else:   # 조건을 만족하지 못한경우
                        break   # 종료

                elif grounds[nr][nc] == '*':   # 벽인 경우
                    break   # 종료

                elif grounds[nr][nc] == 'C':   # 도착지인 경우
                    print(cnt)   # 정답 출력
                    exit(0)   # 프로그램 종료
            else:   # 범위를 벗어난 경우
                break   # 종료


input = sys.stdin.readline
W, H = map(int, input().split())
grounds = [list(input().strip()) for _ in range(H)]   # 놓여있는 상태 저장
cnts = [[float('inf') for _ in range(W)] for _ in range(H)]   # 필요한 거울 최소 갯수 무한으로 초기화
is_visits = [[[False for _ in range(W)] for _ in range(H)] for _ in range(2)]   # 진행방향(세로, 가로)별로 해당 방향으로 지나갔는지를 False로 초기화
targets = []   # 시작점을 담을 리스트
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
q = []   # 계산할 위치를 힙으로 저장할 리스트

for r in range(H):
    for c in range(W):
        if grounds[r][c] == 'C':   # 시작점을 찾아
            targets.append((r, c))   # 저장하고
            break   # 종료

r, c = targets[0]
grounds[r][c] = '*'   # 시작점을 벽으로 만들고
heapq.heappush(q, (-1, r, c))   # 큐에 -1(처음에 4방향별로 다른 것 계산위해), 시작위치 저장

while q:
    cnt, r, c = heapq.heappop(q)   # 큐에서 필요한 거울 수, 위치를 가져온다
    calc(cnt + 1, r, c)   # 필요한 거울 수 + 1하여 계산


# import sys
# import heapq
#
# input = sys.stdin.readline
# W, H = map(int, input().split())
# grounds = [list(input().strip()) for _ in range(H)]
# cnts = [[float('inf') for _ in range(W)] for _ in range(H)]
# targets = []
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
# q = []
#
# for r in range(H):
#     for c in range(W):
#         if grounds[r][c] == 'C':
#             targets.append((r, c))
#
# r, c = targets[0]
# grounds[r][c] = '*'
# heapq.heappush(q, (-1, r, c, 4))
#
# while q:
#     cost, r, c, d = heapq.heappop(q)
#     if grounds[r][c] == 'C':
#         break
#
#     if cnts[r][c] < cost:
#         continue
#
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < H and 0 <= nc < W and grounds[nr][nc] != '*':
#             if d == i and cost <= cnts[nr][nc]:
#                 cnts[nr][nc] = cost
#                 heapq.heappush(q, (cost, nr, nc, i))
#             elif d != i and cost + 1 <= cnts[nr][nc]:
#                 cnts[nr][nc] = cost + 1
#                 heapq.heappush(q, (cost + 1, nr, nc, i))
#
# print(cnts[targets[1][0]][targets[1][1]])


# import sys
# from collections import deque
#
# input = sys.stdin.readline
# W, H = map(int, input().split())
# grounds = [list(input().strip()) for _ in range(H)]
# cnts = [[float('inf') for _ in range(W)] for _ in range(H)]
# targets = []
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
# q = deque([])
#
# for r in range(H):
#     for c in range(W):
#         if grounds[r][c] == 'C':
#             targets.append((r, c))
#
# cnts[targets[0][0]][targets[0][1]] = -1
# q.append(targets[0])
#
# while q:
#     r, c = q.popleft()
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         while True:
#             if not 0 <= nr < H or not 0 <= nc < W:
#                 break
#             if grounds[nr][nc] == '*':
#                 break
#             if cnts[nr][nc] <= cnts[r][c]:
#                 break
#             q.append((nr, nc))
#             cnts[nr][nc] = cnts[r][c] + 1
#             nr += dr[i]
#             nc += dc[i]
#
# print(cnts[targets[1][0]][targets[1][1]])


# from collections import deque
#
# W, H = map(int, input().split())
# grounds = [list(input().strip()) for _ in range(H)]
# targets = []
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
# q = deque([])
#
# for r in range(H):
#     for c in range(W):
#         if grounds[r][c] == 'C':
#             targets.append((r, c))
#         elif grounds[r][c] == '.':
#             grounds[r][c] = float('inf')
#
# grounds[targets[0][0]][targets[0][1]] = -1
# grounds[targets[1][0]][targets[1][1]] = float('inf')
# q.append([targets[0][0], targets[0][1], 4])
#
# while q:
#     r, c, d = q.popleft()
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < H and 0 <= nc < W and grounds[nr][nc] != '*':
#             cnt = grounds[r][c]
#             if i != d:
#                 cnt += 1
#             if cnt <= grounds[nr][nc]:
#                 q.append((nr, nc, i))
#                 grounds[nr][nc] = cnt
#
# print(grounds[targets[1][0]][targets[1][1]])
