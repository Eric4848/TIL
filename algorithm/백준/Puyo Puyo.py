import sys
from collections import deque

input = sys.stdin.readline
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
matrix = [list(input()) for _ in range(12)]
answer = 0


# 연결된 것 확인
def search(R, C):
    q = deque()
    q.append((R, C))   # deque에 입력 위치를 추가
    while q:   # 큐가 비지 않았다면
        row, col = q.popleft()   # popleft해서 row, col 가져온다
        for j in range(4):   # 4방향으로
            nr = row + dr[j]
            nc = col + dc[j]
            # 범위 이내고 방문하지 않은 위치이며 입력 위치와 새 위치의 색상이 같다면
            if 0 <= nr < 12 and 0 <= nc < 6 and not is_visit[nr][nc] and matrix[row][col] == matrix[nr][nc]:
                is_visit[nr][nc] = True   # 새 위치를 방문처리
                q.append((nr, nc))   # 큐에 새 위치 추가
                same.append((nr, nc))   # 같은 색상에 위치 추가


# 제거하는 함수
def delete(remove):
    for R, C in remove:   # 입력된 리스트의 위치별로
        matrix[R][C] = '.'   # '.'로 변경


while True:
    chk = 1   # 터지는 것이 없다
    is_visit = [[False] * 6 for _ in range(12)]   # 방문여부를 False로 설정

    for r in range(12):
        for c in range(6):
            if matrix[r][c] != '.':   # 해당 위치가 비지 않았으면
                is_visit[r][c] = True   # 해당 위치를 방문처리 하고
                same = [(r, c)]   # 같은 색상에 현재 위치 추가
                search(r, c)   # 현재 위치기준으로 연결된 것 확인
                if 4 <= len(same):   # 같은 색상이 4개 이상이면
                    delete(same)   # 같은것들 제거
                    chk = 0   # 터지는 것이 있다

    if chk:   # 터지는 것이 없으면
        break   # 중단
    # 터진 후라면
    answer += 1   # 정답 + 1

    for i in range(6):   # 열별
        for j in range(10, -1, -1):   # 뒤에서 2번째부터 맨 처음행까지(위쪽)
            for k in range(11, j, -1):   # 맨 뒤에서 윗쪽행까지(아래쪽)
                if matrix[j][i] != '.' and matrix[k][i] == '.':   # 위쪽행이 비지 않고, 아래쪽 행이 비었다면
                    matrix[k][i] = matrix[j][i]   # 아래쪽 행에 위쪽 행 저장
                    matrix[j][i] = '.'   # 위쪽행을 비운다
                    break   # 아래쪽 행 탐색 중단

print(answer)
