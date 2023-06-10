from collections import deque

N, M = map(int, input().split())
matrix = [[] for _ in range(N+1)]   # 인덱스 번호를 맞추기 위해 N+1까지 생성
is_linked = [False] * (N+1)   # 연결 여부 확인
answer = 0

for _ in range(M):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)   # 방향이 없는 그래프


def bfs(n):
    links = deque([n])   # 너비 우선 탐색을 위해 deque로 변환
    while links:
        to_visit = links.popleft()
        if not is_linked[to_visit]:
            is_linked[to_visit] = True
            links += deque(matrix[to_visit])   # 연결 후 연결된 요소들을 deque로 변환하여 추가


for i in range(1, N+1):
    if not is_linked[i]:
        bfs(i)   # i가 연결된 정점들을 확인하고 연결여부를 바꾸어준다
        answer += 1   # 연결요수 개수를 1개 늘려준다

print(answer)
