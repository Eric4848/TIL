# 프림 -> 간선이 많을 때 유리
import sys
import heapq

input = sys.stdin.readline
V, E = map(int, input().split())
edges = [[] for _ in range(V+1)]   # 간선을 담을 리스트
is_visit = [False] * (V+1)   # 노드의 방문 여부
q = []   # 힙으로 만들 큐
answer = 0
# 간선들을 저장
for _ in range(E):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

heapq.heappush(q, (0, 1))   # 힙에 비용 0과 임의의 시점을 저장

while q:
    cost, now = heapq.heappop(q)   # 비용과 도착 위치를 불러온다
    if not is_visit[now]:   # 도착 위치가 처음 온 곳이면
        is_visit[now] = True   # 방문처리하고
        answer += cost   # 비용을 추가하고
        for nxt_cost, nxt in edges[now]:   # 도착지의 간선들을
            heapq.heappush(q, (nxt_cost, nxt))   # 힙에 추가한다

print(answer)


# 크루스칼 -> 간선이 적을 때 유리
# 시간초과
# import sys
# import heapq
#
# sys.setrecursionlimit(10 ** 9)
# input = sys.stdin.readline
# V, E = map(int, input().split())
# parents = [i for i in range(V+1)]
# edges = []
# answer = 0
# for _ in range(E):
#     a, b, c = map(int, input().split())
#     heapq.heappush(edges, (c, a, b))
#
#
# def find(n):
#     parent = parents[n]
#     if n != parent:
#         parent = find(parent)
#     return parent
#
#
# def union(A, B):
#     L = find(A)
#     R = find(B)
#     if L < B:
#         parents[R] = L
#     else:
#         parents[L] = R
#
#
# N = 1
# while True:
#     if N == V:
#         break
#
#     cost, a, b = heapq.heappop(edges)
#     if find(a) != find(b):
#         union(a, b)
#         N += 1
#         answer += cost
#
# print(answer)
