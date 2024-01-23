import sys
import heapq

input = sys.stdin.readline
V, E = map(int, input().split())
vils = [[] for _ in range(V+1)]   # 지역별로 이어진 길과 거리를 저장할 리스트
distances = [[float('inf')] * (V+1) for _ in range(V+1)]   # 지역별로 다른 지역과의 최소거리를 무한으로 초기화
q = []   # 힙으로 사용할 리스트
chk = 1

for _ in range(E):
    s, e, d = map(int, input().split())
    vils[s].append([d, e])   # 출발지역에 거리와 도착지점을 저장
    distances[s][e] = d   # 출발지->도착지 위치에 거리 저장
    heapq.heappush(q, (d, s, e))   # 힙에 거리, 출발지, 도착지 저장

while q:
    dist, start, now = heapq.heappop(q)
    if start == now:   # 출발지가 현재 위치와 같다면
        chk = 0   # 체크를 풀고
        print(dist)   # 거리를 출력하고
        break   # 종료

    if distances[start][now] < dist:   # 출발지에서 현재 위치까지 거리가 여태까지 이동거리보다 짧다면
        continue   # 넘어간다

    for nd, nxt in vils[now]:   # 현재 위치에서 이어진 길의 거리와 도착지별로
        if dist + nd < distances[start][nxt]:   # 출발지에서 도착지까지 거리보다 이동거리와 이어진 거리가 짧다면
            distances[start][nxt] = dist + nd   # 거리를 갱신하고
            heapq.heappush(q, (dist + nd, start, nxt))   # 갱신한 거리, 출발위치, 도착지를 힙에 추가한다

if chk:
    print(-1)


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# V, E = map(int, input().split())
# graph = [[float('inf')] * (V+1) for _ in range(V+1)]
#
# for _ in range(E):
#     s, e, d = map(int, input().split())
#     graph[s][e] = d
#
# for k in range(1, V+1):
#     for i in range(1, V+1):
#         for j in range(1, V+1):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
#
# answer = float('inf')
# for i in range(1, V+1):
#     answer = min(answer, graph[i][i])
#
# if answer == float('inf'):
#     print(-1)
# else:
#     print(answer)


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# V, E = map(int, input().split())
# vils = [[] for _ in range(V+1)]
# answer = float('inf')
#
#
# for _ in range(E):
#     s, e, d = map(int, input().split())
#     vils[s].append([e, d])
#
# for i in range(1, V+1):
#     distances = [float('inf')] * (V+1)
#     q = [(0, i)]
#     while q:
#         dist, now = q.pop()
#         if distances[now] < dist:
#             continue
#
#         for nxt in vils[now]:
#             if dist + nxt[1] < distances[nxt[0]]:
#                 distances[nxt[0]] = dist + nxt[1]
#                 q.append((dist + nxt[1], nxt[0]))
#     answer = min(answer, distances[i])
#
# print(answer)


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# V, E = map(int, input().split())
# vils = [[] for _ in range(V+1)]
# answer = float('inf')
#
#
# def search(N, W):
#     if N == i:
#         tmp.append(W)
#         return
#
#     for route in vils[N]:
#         if not is_visit[route[0]] and W + route[1] < answer:
#             is_visit[route[0]] = True
#             search(route[0], W+route[1])
#             is_visit[route[0]] = False
#
#
# for _ in range(E):
#     s, e, d = map(int, input().split())
#     vils[s].append([e, d])
#
# for i in range(1, V+1):
#     is_visit = [False] * (V+1)
#     tmp = []
#     for nxt in vils[i]:
#         search(nxt[0], nxt[1])
#     if tmp:
#         answer = min(answer, min(tmp))
#
# print(answer)
