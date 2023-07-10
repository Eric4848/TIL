import sys
from collections import deque

input = sys.stdin.readline
M, N, H = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]   # 토마토 배열을 입력받음
answer = -1   # 정답을 -1로 초기화 (while문으로 확인하며 1을 증가시키기 때문에 미리 1을 빼줌)

dz = [1, -1, 0, 0, 0, 0]   # z축 변화
dy = [0, 0, 1, -1, 0, 0]   # y축 변화
dx = [0, 0, 0, 0, 1, -1]   # x축 변화

queue = deque()

for i in range(H):   # z축
    for j in range(N):   # y축
        for k in range(M):   # x축
            if matrix[i][j][k] == 1:   # 토마토가 익었으면
                queue.append((i, j, k))   # 추가

while queue:   # 익은 것을 확인한 토마토가 있으면
    answer += 1   # 1일 추가하고
    for _ in range(len(queue)):   # 익은 토마토 갯수만큼
        z, y, x = queue.popleft()   # 익은 토마토를
        for i in range(6):   # 6방향으로
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if -1 < nz < H and -1 < ny < N and -1 < nx < M:
                if matrix[nz][ny][nx] == 0:   # 익지 않았다면
                    matrix[nz][ny][nx] = 1   # 익음 처리하고
                    queue.append((nz, ny, nx))   # 익은 토마토에 추가

check = 0   # 안익는 토마토 확인용
for maty in matrix:
    for matx in maty:
        if 0 in matx:   # 안익은 토마토가 있으면
            check += 1   # check를 1 증가시키고
            break

if check != 0:   # 안익은 토마토가 있으면
    print(-1)   # -1 출력
else:   # 아니면
    print(answer)   # 정답 출력
