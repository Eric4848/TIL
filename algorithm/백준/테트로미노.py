import sys

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = [0]   # 정답을 0으로 초기화 해준다
dr = [1, 0, -1, 0]   # 가로
dc = [0, 1, 0, -1]   # 세로의 이동방향
log = [-1]   # 이동 방향을 저장(4방향 이동중 이전 이동을 제외한 나머지 방향만 가능)


def check(r, c, total):   # ㅜ모양을 제외한 나머지 모양들은 시작점부터 4개의 이어지는 칸들의 합이고 이를 구하는 함수
    if len(log) == 4:   # 이동기록이 1(허구 이동)+3(진짜 이동) = 4회일 때
        if answer[0] < total:   # 총합이 정답보다 크면
            answer[0] = total   # 변경한다
        return

    for i in range(4):
        if (i + 2) % 4 != log[-1]:   # 이번 이동방향의 역방향이 이전 이동방향과 다르다면(이전칸으로 돌아가지 않는다면)
            nr = r + dr[i]   # 다음칸 가로와
            nc = c + dc[i]   # 세로를 설정하고
            if 0 <= nr < N and 0 <= nc < M:   # 범위 이내라면
                log.append(i)   # 이동 기록에 이동 방향을 저장하고
                check(nr, nc, total+matrix[nr][nc])   # 위치를 다음칸으로 변경하고, 총합에 다음칸의 값을 넣어준다
                log.pop()   # 다음칸을 확인한 후 이동 기록에서 지워준다


def chk(r, c):   # ㅜ모양을 구하는 함수
    for i in range(4):   # 각 방향별로
        total = matrix[r][c]   # ㅜ모양 총합을 현위치로 초기화 한다
        for j in range(3):   # 가운데 기준으로 시계방향으로 1칸씩 3번 이동한 칸들의 합
            nxt = (i+j) % 4   # 다음 칸의 위치를 시작방향기준으로 1칸씩 늘려가며 결정
            nr = r + dr[nxt]   # 다음칸 가로와
            nc = c + dc[nxt]   # 세로를 설정하고
            if 0 <= nr < N and 0 <= nc < M:   # 범위 이내면
                total += matrix[nr][nc]   # 총합에 추가한다
            else:   # 범위를 벗어나는 것이 있는 경우
                break   # 중단한다
        if answer[0] < total:   # 정답보다 총합이 크다면(3방향을 계산중 중간에 멈춘다 해도 첫번째 확인에서 나머지 모양을 만들 수 있으므로 중단되었는지 계산하지 않아도 된다)
            answer[0] = total   # 변경한다


for i in range(N):   # 각 칸별로
    for j in range(M):
        check(i, j, matrix[i][j])   # 모든 모양을
        chk(i, j)   # 확인해 준 후

print(answer[0])   # 정답을 출력한다


# ㅜ 모양 확인 불가
# import sys
#
# sys.setrecursionlimit(10 ** 9)
# N, M = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(N)]
# answer = [0]
# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]
# log = [-1]
#
#
# def check(r, c, total):
#     if len(log) == 4:
#         if answer[0] < total:
#             answer[0] = total
#         return
#
#     for i in range(4):
#         if (i + 2) % 4 != log[-1]:
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nr < N and 0 <= nc < M:
#                 log.append(i)
#                 check(nr, nc, total+matrix[nr][nc])
#                 log.pop()
#
#
# for i in range(N):
#     for j in range(M):
#         check(i, j, matrix[i][j])
#
# print(answer[0])


# 메모리 초과
# import sys
#
# sys.setrecursionlimit(10 ** 9)
# N, M = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(N)]
# answer = [0]
# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]
#
#
# def check(r, c, d, total, b):
#     if d == 4:
#         if answer[0] < total:
#             answer[0] = total
#             return
#
#     for i in range(4):
#         if i + 2 % 4 != b:
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nr < N and 0 <= nc < M:
#                 check(nr, nc, d+1, total+matrix[nr][nc], i)
#
#
# for i in range(N):
#     for j in range(M):
#         check(i, j, 1, matrix[i][j], 4)
#
# print(answer[0])

# 시간 초과
# import sys
#
# sys.setrecursionlimit(10 ** 9)
# N, M = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(N)]
# answer = [0]
# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]
# is_visit = [[False] * M for _ in range(N)]
#
#
# def check(r, c, d, total):
#     if d == 4:
#         if answer[0] < total:
#             answer[0] = total
#
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < N and 0 <= nc < M:
#             if not is_visit[nr][nc]:
#                 is_visit[nr][nc] = True
#                 check(nr, nc, d+1, total+matrix[nr][nc])
#                 is_visit[nr][nc] = False
#
#
# for i in range(N):
#     for j in range(M):
#         is_visit[i][j] = True
#         check(i, j, 1, matrix[i][j])
#         is_visit[i][j] = False
#
# print(answer[0])
