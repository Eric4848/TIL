# 시간 초과
import sys

input = sys.stdin.readline
V, E = map(int, input().split())
graph = [[float('inf')] * (V+1) for _ in range(V+1)]

for _ in range(E):
    s, e, d = map(int, input().split())
    graph[s][e] = d

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = float('inf')
for i in range(1, V+1):
    for j in range(1, V+1):
        answer = min(answer, graph[i][j] + graph[j][i])

if answer == float('inf'):
    print(-1)
else:
    print(answer)


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
