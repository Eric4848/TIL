import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
N = int(input())
mat = [list(input()) for _ in range(N)]
answer = [0, 0]   # 비색약, 색약일 때의 갯수를 0개로 초기화
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def search(r, c, t):   # 이어진 것 확인하는 함수
    is_count[r][c] = True   # 입력 위치를 확인처리
    for i in range(4):   # 4방향으로
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:   # 범위 내에 있고
            if mat[nr][nc] in t and not is_count[nr][nc]:   # 그 위치가 목표 색상 리스트 내에 있고, 확인하지 않았다면
                search(nr, nc, t)   # 그 위치 다시 확인


is_count = [[False] * N for _ in range(N)]   # N X N의 확인 여부 초기화
for R in range(N):
    for C in range(N):
        if mat[R][C] == 'B' and not is_count[R][C]:   # 현재 위치가 파란색이고 확인하지 않았다면
            search(R, C, ['B'])   # 파란색으로 이어진 것을 확인하고
            answer[0] += 1   # 비색약과
            answer[1] += 1   # 색약인 경우 모두 1개씩 추가
        elif not is_count[R][C]:   # 그외 의 경우 확인하지 않은 곳이라면
            search(R, C, ['R', 'G'])   # 빨강과 녹색으로 이어진 것을 확인하고
            answer[1] += 1   # 색약인 경우 1개 추가

is_count = [[False] * N for _ in range(N)]   # 확인여부를 다시 초기화
for R in range(N):
    for C in range(N):
        if mat[R][C] == 'R' and not is_count[R][C]:   # 현재 위치가 빨간색이고 확인하지 않았다면
            search(R, C, ['R'])   # 빨간색으로 이어진 것을 확인하고
            answer[0] += 1   # 비색약 1개 추가
        elif mat[R][C] == 'G' and not is_count[R][C]:   # 빨간색과 마찬가지
            search(R, C, ['G'])
            answer[0] += 1

print(*answer)
