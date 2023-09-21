import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
K = int(input())


def check(start, group):
    groups[start] = group  # 현재 노드의 그룹 저장

    for i in graph[start]:   # 현재와 연결 된 모든노드별로
        if groups[i] == 0:  # 아직 그룹이 정해지지 않았다면 노드
            result = check(i, -group)   # 반대 그룹으로 확인 진행
            if not result:   # 확인 결과 아닌 경우
                return False   # 아니라고 반환
        else:   # 그룹이 정해진 노드의 경우
            if groups[i] == group:  # 이미 방문한 곳 중에서 노드가 현재 그룹과 같으면 이분 그래프가 아님
                return False   # 아니라고 반환
    return True   # 아닌 경우들을 제외하곤 맞다고 반환


for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]   # 연결 노드들을 저장할 리스트를 0~V까지 생성한다
    groups = [0] * (V + 1)   # 각 노드별 그룹을 0으로 초기화 한다
    for _ in range(E):   # 간선들을 넣어준다
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, V + 1):   # 모든 노드별로(모두 하나의 노드가 아닐 수도 있기 때문)
        if groups[i] == 0:   # 그룹이 정해지지 않았다면
            result = check(i, 1)   # 1번 그룹으로 가정하고 확인 진행하여 저장
            if not result:   # 확인 결과 이분 그래프가 아닌경우
                break   # 중단한다

    if result:
        print('YES')
    else:
        print('NO')

# 시간초과
# K = int(input())
#
#
# def check(n, d, s):
#     if s == n:
#         if d != 0 and d % 2 == 1:
#             odd[0] = 1
#             return
#     for i in range(len(graph[n])):
#         nxt = graph[n][i]
#         if not is_visited[nxt]:
#             is_visited[nxt] = True
#             check(nxt, d+1, s)
#             is_visited[nxt] = False
#
#
# for _ in range(K):
#     V, E = map(int, input().split())
#     graph = [[] for _ in range(V+1)]
#     chk = 0
#     for _ in range(E):
#         u, v = map(int, input().split())
#         graph[u].append(v)
#         graph[v].append(u)
#
#     for i in range(1, V + 1):
#         odd = [0]
#         is_visited = [False] * (V+1)
#         check(i, 0, i)
#         if odd[0] == 1:
#             chk = 1
#             print('NO')
#             break
#     if chk == 0:
#         print('YES')
