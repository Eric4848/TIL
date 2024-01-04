import sys

sys.setrecursionlimit(10 ** 6)
M, N, K = map(int, input().split())
matrix = [[0] * N for _ in range(M)]  # 주어진 크기를 0으로 초기화 한 리스트
answers = []  # 정답을 담을 리스트
for _ in range(K):
    lc, lr, rc, rr = map(int, input().split())  # 좌측 하단 x, y / 우측 상단 x, y
    for r in range(lr, rr):  # 좌측 하단 y ~ 우측 상단 y(그래프를 상하 반전하여 계산)
        for c in range(lc, rc):  # 좌측 하단 x ~ 우측 상단 x
            matrix[r][c] = 1  # 주어진 범위를 1로 변경

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


# 입력 위치를 받아 크기를 계산하는 함수
def find(R, C):
    matrix[R][C] = 1  # 입력 위치를 1로 변경
    answers[-1] += 1  # 정답을 1 늘려준다
    for i in range(4):  # 4방향으로
        nr = R + dr[i]
        nc = C + dc[i]
        if 0 <= nr < M and 0 <= nc < N and not matrix[nr][nc]:  # 범위 이내고 분리된 영역이면
            find(nr, nc)  # 해당 위치에서 추가로 계산


for r in range(M):
    for c in range(N):
        if matrix[r][c] == 0:  # 분리된 영역이면
            answers.append(0)  # 정답에 0을 추가하고
            find(r, c)  # 해당 위치부터 계산

answers.sort()  # 정답을 정렬
print(len(answers))
print(*answers)
