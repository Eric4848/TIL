import copy   # 그래프를 객체까지 모두 복사할 deepcopy사용을 위해 추가
n, m = map(int, input().split())
cctv = []
graph = []
# CCTV 숫자별 확인 방향
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

# 북 - 동 - 남 - 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):   # 그래프 입력
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:   # CCTV위치 확인
            cctv.append([data[j], i, j])   # CCTV번호와 위치 저장


# CCTV확인하는 영역 채우는 함수
def fill(board, mm, x, y):
    for i in mm:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:   # 범위를 벗어나면
                break   # 중단
            if board[nx][ny] == 6:   # 벽에 만나면
                break   # 중단
            elif board[nx][ny] == 0:   # 빈공간이면
                board[nx][ny] = 7   # 7로 변경


def dfs(depth, arr):
    global min_value

    if depth == len(cctv):   # 모든 CCTV를 확인했으면
        count = 0   # 현재 사각지대를 0으로 초기화
        for i in range(n):
            count += arr[i].count(0)   # 각 줄별로 사각지대를 더해준다
        min_value = min(min_value, count)   # 정답과 비교하여 작은 값 저장
        return   # 종료
    temp = copy.deepcopy(arr)   # 입력된 CCTV감시상태를 복사
    cctv_num, x, y = cctv[depth]   # 깊이+1번째 카메라의 번호와 위치를 불러와서
    for cm in mode[cctv_num]:   # 카메라의 범위별로
        fill(temp, cm, x, y)   # 감시영역을 채우고
        dfs(depth+1, temp)   # 채운 영역을 다음 dfs로 넘겨준다
        temp = copy.deepcopy(arr)   # 감시상태를 다시 복사해온다


min_value = int(1e9)   # 정답을 10의 9승으로 초기화
dfs(0, graph)
print(min_value)


# 오답
# N, M = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(N)]
# camera = []
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]
#
#
# def count():
#     counts = 0
#     for i in range(N):
#         for j in range(M):
#             if matrix[i][j] == 0:
#                 counts += 1
#     return counts
#
#
# answer = [count()]
# for i in range(N):
#     for j in range(M):
#         if 0 < matrix[i][j] < 6:
#             camera.append((i, j, matrix[i][j]))
#
#
# def dfs(d):
#     if d == cams:
#         answer[0] = min(answer[0], count())
#         print(matrix)
#         return
#     r, c, a = camera[d]
#     if a == 1:
#         for i in range(4):
#             nr = r
#             nc = c
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 0:
#                         matrix[nr][nc] = 7
#                     nr += dr[i]
#                     nc += dc[i]
#             dfs(d+1)
#             nr = r
#             nc = c
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 7:
#                         matrix[nr][nc] = 0
#                     nr += dr[i]
#                     nc += dc[i]
#
#     elif a == 2:
#         for i in range(2):
#             nr = r
#             nc = c
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 0:
#                         matrix[nr][nc] = 7
#                     nr += dr[i]
#                     nc += dc[i]
#             nr = r
#             nc = c
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 0:
#                         matrix[nr][nc] = 7
#                     nr += dr[i + 2]
#                     nc += dc[i + 2]
#             dfs(d+1)
#             nr = r
#             nc = c
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 7:
#                         matrix[nr][nc] = 0
#                     nr += dr[i]
#                     nc += dc[i]
#             nr = r
#             nc = c
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 7:
#                         matrix[nr][nc] = 0
#                     nr += dr[i + 2]
#                     nc += dc[i + 2]
#
#     elif a == 3:
#         for i in range(4):
#             nr = r
#             nc = c
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 0:
#                         matrix[nr][nc] = 7
#                     nr += dr[i]
#                     nc += dc[i]
#             nr = r
#             nc = c
#             nxt = (i + 1) % 4
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 0:
#                         matrix[nr][nc] = 7
#                     nr += dr[nxt]
#                     nc += dc[nxt]
#             dfs(d + 1)
#             nr = r
#             nc = c
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 7:
#                         matrix[nr][nc] = 0
#                     nr += dr[i]
#                     nc += dc[i]
#             nr = r
#             nc = c
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 7:
#                         matrix[nr][nc] = 0
#                     nr += dr[nxt]
#                     nc += dc[nxt]
#
#     elif a == 4:
#         for i in range(4):
#             nr = r
#             nc = c
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 0:
#                         matrix[nr][nc] = 7
#                     nr += dr[i]
#                     nc += dc[i]
#             nr = r
#             nc = c
#             nxt = (i + 1) % 4
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 0:
#                         matrix[nr][nc] = 7
#                     nr += dr[nxt]
#                     nc += dc[nxt]
#             nr = r
#             nc = c
#             nxt2 = (i + 2) % 4
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 0:
#                         matrix[nr][nc] = 7
#                     nr += dr[nxt2]
#                     nc += dc[nxt2]
#             dfs(d + 1)
#             nr = r
#             nc = c
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 7:
#                         matrix[nr][nc] = 0
#                     nr += dr[i]
#                     nc += dc[i]
#             nr = r
#             nc = c
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 7:
#                         matrix[nr][nc] = 0
#                     nr += dr[nxt]
#                     nc += dc[nxt]
#             nr = r
#             nc = c
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 7:
#                         matrix[nr][nc] = 0
#                     nr += dr[nxt2]
#                     nc += dc[nxt2]
#
#     elif a == 5:
#         for i in range(4):
#             nr = r
#             nc = c
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 0:
#                         matrix[nr][nc] = 7
#                     nr += dr[i]
#                     nc += dc[i]
#             nr = r
#             nc = c
#             nxt = (i + 1) % 4
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 0:
#                         matrix[nr][nc] = 7
#                     nr += dr[nxt]
#                     nc += dc[nxt]
#             nr = r
#             nc = c
#             nxt2 = (i + 2) % 4
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 0:
#                         matrix[nr][nc] = 7
#                     nr += dr[nxt2]
#                     nc += dc[nxt2]
#             nr = r
#             nc = c
#             nxt3 = (i + 3) % 4
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 0:
#                         matrix[nr][nc] = 7
#                     nr += dr[nxt3]
#                     nc += dc[nxt3]
#             dfs(d + 1)
#             nr = r
#             nc = c
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 7:
#                         matrix[nr][nc] = 0
#                     nr += dr[i]
#                     nc += dc[i]
#             nr = r
#             nc = c
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 7:
#                         matrix[nr][nc] = 0
#                     nr += dr[nxt]
#                     nc += dc[nxt]
#             nr = r
#             nc = c
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 7:
#                         matrix[nr][nc] = 0
#                     nr += dr[nxt2]
#                     nc += dc[nxt2]
#             nr = r
#             nc = c
#             while 0 <= nr < N and 0 <= nc < M:
#                 if matrix[nr][nc] == 6:
#                     break
#                 else:
#                     if matrix[nr][nc] == 7:
#                         matrix[nr][nc] = 0
#                     nr += dr[nxt3]
#                     nc += dc[nxt3]
#
#
# cams = len(camera)
# dfs(0)
# print(answer[0])
