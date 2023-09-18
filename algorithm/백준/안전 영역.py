import sys

sys.setrecursionlimit(10 ** 6)   # 재귀 깊이 때문에 오류 발생 -> 재귀 깊이 늘려준다
N = int(input())
grounds = [list(map(int, input().split())) for _ in range(N)]
answer = 0
maximum = 0   # 가장 높은 지역을 찾아준다
for i in range(N):
    if maximum < max(grounds[i]):
        maximum = max(grounds[i])

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def check(r, c, n):   # 입력된 위치부터 사방으로 같은 육지인지 확인
    for i in range(4):   # 4방향으로
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and not is_visit[nr][nc]:   # 땅 범위 이내면서 방문하지 않은 지역이면
            if n < grounds[nr][nc]:   # 설정된 물 높이보다 높다면
                is_visit[nr][nc] = True   # 방문처리 하고
                check(nr, nc, n)   # 그 지역도 확인


for i in range(maximum):   # 물의 높이별로
    is_visit = [[0] * N for _ in range(N)]   # 방문 기록을 초기화 하고
    total = 0   # 총 섬의 갯수도 초기화한다
    for r in range(N):   # 모든 위치별로
        for c in range(N):
            if i < grounds[r][c] and not is_visit[r][c]:   # 그 위치가 물보다 높고 방문하지 않았다면
                total += 1   # 섬의 갯수를 늘려주고
                is_visit[r][c] = True   # 방문처리 한 후
                check(r, c, i)   # 그 섬과 한 섬들을 찾아서 방문처리한다

    answer = max(answer, total)   # 물 높이별로 섬 갯수가 높은 것을 선택한다

print(answer)
