# 프림(Prim)
import sys
import heapq

input = sys.stdin.readline
N = int(input())
M = int(input())
lines = [[] for _ in range(N+1)]
is_visited = [False for _ in range(N+1)]
answer = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    lines[a].append((c, b))
    lines[b].append((c, a))

q = []
heapq.heappush(q, (0, 1))

while q:
    weight, now = heapq.heappop(q)
    if not is_visited[now]:
        is_visited[now] = True
        answer += weight
        for nxt_weight, nxt in lines[now]:
            heapq.heappush(q, (nxt_weight, nxt))
print(answer)


# 크루스칼(Kruskal)
# import sys
#
# input = sys.stdin.readline
# N = int(input())
# M = int(input())
#
#
# def find(x):
#     if x != computers[x]:
#         computers[x] = find(computers[x])
#     return computers[x]
#
#
# def union(x, y):
#     x = find(x)
#     y = find(y)
#     if x < y:
#         computers[y] = x
#     else:
#         computers[x] = y
#
#
# computers = [i for i in range(N+1)]
# lines = [list(map(int, input().split())) for _ in range(M)]
# is_used = [False for _ in range(M)]
# lines.sort(key=lambda x: x[2], reverse=True)
# cnt = 1
# answer = 0
# while cnt != N:
#     a, b, c = lines.pop()
#     if find(a) == find(b):
#         continue
#     union(a, b)
#     answer += c
#     cnt += 1
# print(answer)


# 실패 - 연결 N-1개만 찾는 방식 - 최소가 아니다
# N-1개의 연결이 최소이다. 적절한 간선들을 선택하지 못하는 문제
# 시간 초과 - 간선들을 가중치 순으로 정렬 시 제대로 선택
# import sys
#
# sys.setrecursionlimit(10 ** 9)
# N = int(input())
# M = int(input())
# computers = [False for _ in range(N+1)]
# answer = [float('inf')]
# lines = [list(map(int, input().split())) for _ in range(M)]
# lines.sort(key=lambda x: x[2])
# is_used = [False for _ in range(M)]
#
#
# def search(i, cost):
#     if answer[0] < cost:
#         return
#     if sum(computers) == N:
#         if cost < answer[0]:
#             answer[0] = cost
#         return
#
#     a, b, c = lines[i]
#
#     if computers[a] and not computers[b]:
#         for j in range(M):
#             if not is_used[j]:
#                 is_used[j] = True
#                 computers[b] = True
#                 search(j, cost+c)
#                 is_used[j] = False
#                 computers[b] = False
#
#     elif computers[b] and not computers[a]:
#         for j in range(M):
#             if not is_used[j]:
#                 is_used[j] = True
#                 computers[a] = True
#                 search(j, cost+c)
#                 is_used[j] = False
#                 computers[a] = False
#
#
# for k in range(M):
#     A, B, C = lines[k]
#     is_used[k] = True
#     computers[A] = True
#     computers[B] = True
#     search(0, C)
#     is_used[k] = False
#     computers[A] = False
#     computers[B] = False
# print(answer[0])
