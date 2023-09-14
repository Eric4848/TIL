N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = [float('inf')]   # 정답을 무한으로 초기화
is_been = [False] * N   # 방문여부를 안함으로 초기화
is_been[0] = True   # 맨 처음 도시를 기준으로 하기 위해 방문 처리를 한다


def dfs(now, total, d):   # 현재위치, 총 이동거리, 이동 횟수
    if d == N-1:   # 도시수 - 1번(원래 도시로 돌아오는 것을 제외한 횟수)만큼 이동 했으면
        if matrix[now][0]:   # 그 도시에서 처음 도시로 돌아올 수 있다면
            total += matrix[now][0]   # 총 이동거리에 첫 도시로 돌아오는 것을 추가
            if total < answer[0]:   # 정답보다 총 이동거리가 작다면
                answer[0] = total   # 정답을 변경한다
                return

    for nxt in range(N):   # 다음 도시들 후보 중
        if not is_been[nxt]:   # 방문하지 않은 도시이고
            if matrix[now][nxt] != 0:   # 그 도시로 갈 수 있다면
                is_been[nxt] = True   # 그 도시에 방문 표시를 하고
                dfs(nxt, total + matrix[now][nxt], d + 1)   # 이동 거리를 더하고 이동 횟수를 늘려서 다음 반복으로 넘겨준다
                is_been[nxt] = False   # 방문 표시를 지워준다


dfs(0, 0, 0)   # dfs를 실행한다

print(answer[0])
