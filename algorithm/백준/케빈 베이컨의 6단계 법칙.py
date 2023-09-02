from collections import deque

N, M = map(int, input().split())
matrix = [[] for _ in range(N+1)]
answer = [float('inf'), 0]   # 최솟값을 구하기 때문에 정답을 무한으로 초기화 하고 시작 위치를 0으로 초기화한다
for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)


def bfs(start):
    counts = [0] * (N+1)   # 친구이기 위한 다리 수를 0으로 초기화 하여 N+1개 만들어 준다
    q = deque()   # bfs를 진행할 deque
    is_visited = [False] * (N+1)   # 방문 여부를 초기화 한다
    is_visited[start] = True   # 시작 친구를 이미 방문했다고 표시해준다
    q.append(start)   # 큐에 시작 친구를 추가해 준다
    while q:
        now = q.popleft()   # 확인할 친구
        for i in matrix[now]:   # 확인할 친구의 친구들 중에
            if not is_visited[i]:   # 방문하지 않았다면
                counts[i] = counts[now] + 1   # 확인할 친구보다 한다리 더 필요하다고 저장하고
                q.append(i)   # 큐에 추가한 후
                is_visited[i] = True   # 방문했다고 표시한다
    if sum(counts) < answer[0]:   # 친구이기 위한 다리수의 합이 정답보다 작다면
        answer[0] = sum(counts)   # 정답과
        answer[1] = start   # 정답 친구를 변경한다


for i in range(1, N+1):   # 각 친구별로
    bfs(i)   # bfs를 진행한다
print(answer[1])
