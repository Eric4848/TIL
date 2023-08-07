# KeyboardInterrupt
N, M = map(int, input().split())
r, c, d = map(int, input().split())
dr = [-1, 0, 1, 0]   # 북, 동, 남, 서 순서대로 방향 설정
dc = [0, 1, 0, -1]
answer = 0
total = 0
matrix = [list(map(int, input().split())) for _ in range(N)]

for i in range(M):
    total += sum(matrix[i])   # 전체 중 벽이 몇칸인지 더한다

while total != (N * M):   # 벽 + 청소한 구역 갯수가 N X M과 같아지기 전까지
    if matrix[r][c] == 0:   # 현 위치가 청소되지 않았으면
        total += 1   # 구역수를 1 더한다
        answer += 1   # 정답을 1 늘려준다
        matrix[r][c] = 2   # 청소 한 칸을 2로 변경한다

    chk = 0   # 청소할 구역이 없다는 것을 0으로 저장
    for _ in range(4):   # 4방면으로
        d -= 1   # 방향설정의 역순으로
        if d < 0:   # 방향이 0보다 작으면
            d += 4   # 4를 더해 0~3 범위로 넣어준다

        nr = r + dr[d]   # 해당 방향이
        nc = c + dc[d]   # 방향을 구할 때 인덱스를 고려하지 않는 이유는 1인 벽으로 둘러쌓여 0인 지점은 반드시 1칸의 여유가 있기 때문

        if matrix[nr][nc] == 0:   # 청소되어있지 않다면
            r = nr   # 그곳으로 이동하고
            c = nc
            chk = 1   # 청소할 구역이 있다고 바꾼다
            break

    if not chk:   # 청소할 구역이 없다면
        nr = r - dr[d]   # 뒷방향에
        nc = c - dc[d]
        if matrix[nr][nc] == 1:   # 벽이 있는 경우
            break   # 탐색을 중지한다
        else:
            r = nr
            c = nc
print(answer)
