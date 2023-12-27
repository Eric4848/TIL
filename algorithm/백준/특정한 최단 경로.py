import sys
import heapq

input = sys.stdin.readline
N, E = map(int, input().split())
edges = [[] for _ in range(N+1)]   # 간선들을 담을 리스트
# 간선을 저장한다
for _ in range(E):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
    edges[b].append([a, c])

v1, v2 = map(int, input().split())
answer1, answer2 = 0, 0   # v1 -> v2, v2 -> v1의 경우의 거리를 0으로 초기화


# 다익스트라 함수
def dijkstra(start):   # 출발 위치를 인자로 받음
    q = []   # 힙을 담을 리스트
    distances[start] = 0   # 출발 위치까지의 거리를 0으로 변경
    heapq.heappush(q, (0, start))   # 힙에 거리 0과 시작 위치를 저장

    while q:
        dist, now = heapq.heappop(q)   # 현재까지 이동한 거리, 현재 위치를 힙에서 뽑는다

        if distances[now] < dist:   # 현재 위치까지의 거리가 이동한 거리보다 짧다면
            continue   # 넘어간다

        for edge in edges[now]:   # 아닌경우 현재 위치의 간선마다
            if dist + edge[1] < distances[edge[0]]:   # 현재까지의 거리 + 목적지까지 거리가 저장된 목적지까지 거리보다 짧다면
                distances[edge[0]] = dist + edge[1]   # 저장된 값을 변경하고
                heapq.heappush(q, (dist + edge[1], edge[0]))   # 큐에 변경한 이동 거리와 도착지를 저장한다


distances = [float('inf')] * (N + 1)   # 거리를 담을 리스트를 무한으로 초기화
dijkstra(1)   # 출발지 1에서의 다익스트라 계산
answer1 = distances[v1]   # v1까지의 거리
answer2 = distances[v2]   # v2까지의 거리


distances = [float('inf')] * (N + 1)   # 리스트 초기화
dijkstra(N)   # 출발지 N(최종 목적지)에서의 다익스트라 계산
answer1 += distances[v2]   # v2까지의 거리(v2 -> 목적지)를 더한다
answer2 += distances[v1]   # v1까지의 거리(v1 -> 목적지)를 더한다


distances = [float('inf')] * (N + 1)   # 리스트 초기화
dijkstra(v1)   # v1에서의 다익스트라 계산


if answer1 == answer2 == float('inf') or distances[v2] == float('inf'):   # 두 정답의 결과가 모두 무한이거나 v1 <-> v2의 거리가 무한이면
    print(-1)   # 불가능
else:   # 아닌 경우
    print(min(answer1, answer2) + distances[v2])   # 둘 중 짧은 길 + 두 정점의 길 출력

# 시간 초과
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# N, E = map(int, input().split())
# edges = [[] for _ in range(N+1)]
# for _ in range(E):
#     a, b, c = map(int, input().split())
#     edges[a].append([c, b])
#     edges[b].append([c, a])
#
# v1, v2 = map(int, input().split())
# answer1, answer2 = 0, 0
#
# answers = [float('inf')] * (N+1)
# answers[0] = 0
# q = deque([[0, 1, 0]])
# while q:
#     cost, end, start = q.popleft()
#     if answers[start] + cost < answers[end]:
#         answers[end] = answers[start] + cost
#         for c, e in edges[end]:
#             q.append((c, e, end))
#
# answer1 = answers[v1]
# answer2 = answers[v2]
#
# answers = [float('inf')] * (N+1)
# answers[0] = 0
# q = deque([[0, N, 0]])
# while q:
#     cost, end, start = q.popleft()
#     if answers[start] + cost < answers[end]:
#         answers[end] = answers[start] + cost
#         for c, e in edges[end]:
#             q.append((c, e, end))
#
# answer1 += answers[v2]
# answer2 += answers[v1]
#
# answers = [float('inf')] * (N+1)
# answers[0] = 0
# q = deque([[0, v1, 0]])
# while q:
#     cost, end, start = q.popleft()
#     if answers[start] + cost < answers[end]:
#         answers[end] = answers[start] + cost
#         for c, e in edges[end]:
#             q.append((c, e, end))
#
# if answer1 == answer2 == float('inf'):
#     print(-1)
# else:
#     print(min(answer1, answer2) + answers[v2])
