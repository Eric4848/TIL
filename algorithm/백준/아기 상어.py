import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
fields = [list(map(int, input().split())) for _ in range(N)]
answer = 0
size = 2   # 상어의 크기
ate = 0   # 먹은 물고기 수
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for i in range(N):
    for j in range(N):
        if fields[i][j] == 9:    # 상어의 위치를 찾아 저장하고
            y = i
            x = j
            fields[i][j] = 0   # 빈 공간으로 바꿔준다
            break


# 물고기를 찾는 함수
def serach(y, x):
    visits = [[0] * N for _ in range(N)]   # 방문 여부를 0으로 초기화
    q = deque([(y, x)])   # 입력 위치를 deque에 추가
    ables = []   # 가능한 위치들을 담을 리스트
    visits[y][x] = 1   # 입력위치를 1로 변경

    while q:
        r, c = q.popleft()
        # 4방향으로
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and visits[nr][nc] == 0:   # 범위 내 방문하지 않은 곳이라면
                if 0 < fields[nr][nc] < size:   # 먹을 수 있는 물고기인 경우
                    ables.append((visits[r][c], nr, nc))   # 가능한 리스트에 거리, 위치를 저장
                elif fields[nr][nc] == size or fields[nr][nc] == 0:   # 지나갈 수 있는 경우
                    visits[nr][nc] = visits[r][c] + 1   # 해당 위치에 이전 위치 + 1을 저장
                    q.append((nr, nc))   # 큐에 위치 추가
                # if fields[nr][nc] <= size:
                #     q.append((nr, nc))
                #     visits[nr][nc] = visits[r][c] + 1
                #     if 0 < fields[nr][nc] < size:
                #         return nr, nc, visits[nr][nc] - 1

    # 확인이 끝난 후 거리가 큰 경우, 더 아래인 경우, 더 오른쪽인 경우를 기준으로 정렬하여 반환
    return sorted(ables, key=lambda x: (x[0], x[1], x[2]), reverse=True)


while True:
    # 가능한 경우들을 계산하여 저장
    ables = serach(y, x)

    # 가능한 경우가 없으면 중단
    if not ables:
        break
    # 가능한 경우중 pop(역으로 정렬했으므로 뒤에서 뽑는다)
    move, ny, nx = ables.pop()

    answer += move   # 정답에 이동거리를 더한다
    fields[ny][nx] = 0   # 해당 위치를 빈공간으로 바꾼다
    ate += 1   # 먹은 횟수를 1 늘린다
    if ate == size:   # 크기만큼 먹었으면
        size += 1   # 크기를 키우고
        ate = 0   # 먹은 횟수를 0으로 초기화
    y, x = ny, nx   # 위치를 갱신

print(answer)


# import sys
# from collections import deque
#
# input = sys.stdin.readline
# N = int(input())
# fields = [list(map(int, input().split())) for _ in range(N)]
# answer = [0, 0]
# dr = [-1, 0, 0, 1]
# dc = [0, -1, 1, 0]
# for r in range(N):
#     for c in range(N):
#         if fields[r][c] == 9:
#             q = deque([(r, c, 2, 0, 0, 0)])
#             break
#
# while q:
#     r, c, body, ate, move, cnt = q.popleft()
#     # print(r, c)
#     if move == N**2-1:
#         continue
#     if answer[0] < ate:
#         answer = [ate, move]
#     # if answer[0] == ate and move < answer[1]:
#     #     answer[1] = move
#
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < N and 0 <= nc < N:
#             if 0 < fields[nr][nc] < body:
#                 print(nr, nc)
#                 fields[nr][nc] = 0
#                 ate += 1
#                 cnt += 1
#                 if body == cnt:
#                     body += 1
#                     cnt = 0
#                 q = deque([(nr, nc, body, ate, move+1, cnt)])
#
#             elif fields[nr][nc] == body or fields[nr][nc] == 0:
#                 q.append((nr, nc, body, ate, move+1, cnt))
# print(answer[0], answer[1])
