import sys
import math


# 부모를 찾는 함수
def find(n):
    parent = parents[n]
    if parent != n:
        parent = find(parent)
    return parent


# 두 부모를 작은쪽으로 합치는 함수
def union(a, b):
    A = find(a)
    B = find(b)
    if A < B:
        parents[B] = A
    else:
        parents[A] = B


input = sys.stdin.readline
N, M = map(int, input().split())
locs = [[]] + [list(map(int, input().split())) for _ in range(N)]   # 위치를 입력받음
parents = [i for i in range(N + 1)]   # 부모를 자신으로 초기화
dists = []   # 거리들을 담을 리스트
answer = 0.0   # 정답을 0.0으로 초기화

# 이미 이어진 것 계산
for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

# 이어지지 않은 것들의 거리 계산
for i in range(1, N):   # 시작점
    for j in range(i + 1, N + 1):   # 도착점
        if find(i) == find(j):   # 둘이 이어져 있으면
            continue   # 넘어간다
        x1, y1 = locs[i]
        x2, y2 = locs[j]
        dist = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))   # 거리를 계산하여
        dists.append((dist, i, j))   # 거리 리스트에 시작, 도착점과 함께 저장

dists.sort()   # 거리정보 정렬

for dist, a, b in dists:
    if find(a) != find(b):   # 두 지점이 연결되지 않았다면
        answer += dist   # 거리 추가
        union(a, b)   # 지점 연결

print(format(answer, ".2f"))    # 소수점 2째자리까지 출력


# import sys
# import heapq
# import math
#
#
# def find(n):
#     parent = parents[n]
#     if parent != n:
#         parent = find(parent)
#     return parent
#
#
# def union(a, b):
#     A = find(a)
#     B = find(b)
#     if A < B:
#         parents[B] = A
#     else:
#         parents[A] = B
#
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# locs = [[]] + [list(map(int, input().split())) for _ in range(N)]
# parents = [i for i in range(N+1)]
# dists = []
# answer = 0.0
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     union(a, b)
#
# for i in range(1, N):
#     for j in range(i+1, N+1):
#         if find(i) == find(j):
#             continue
#         x1, y1 = locs[i]
#         x2, y2 = locs[j]
#         dist = math.sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))
#         heapq.heappush(dists, (dist, i, j))
#
# linked = M
# while linked < N-1 and dists:
#     dist, a, b = heapq.heappop(dists)
#     if find(a) != find(b):
#         answer += dist
#         union(a, b)
#         linked += 1
#
# print(format(answer, ".2f"))


# import sys
# import heapq
#
#
# def find(n):
#     parent = parents[n]
#     if parent != n:
#         parent = find(parent)
#     return parent
#
#
# def union(a, b):
#     A = find(a)
#     B = find(b)
#     if A < B:
#         parents[B] = A
#     else:
#         parents[A] = B
#
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# locs = [[]] + [list(map(int, input().split())) for _ in range(N)]
# parents = [i for i in range(N+1)]
# dists = []
# is_visit = [False for _ in range(N+1)]
# answer = 0.0
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     is_visit[a] = True
#     is_visit[b] = True
#     union(a, b)
#
# for i in range(1, N):
#     for j in range(i+1, N+1):
#         if is_visit[i] and is_visit[j]:
#             continue
#         x1, y1 = locs[i]
#         x2, y2 = locs[j]
#         dist = ((x1-x2) ** 2 + (y1-y2) ** 2) ** 0.5
#         heapq.heappush(dists, (dist, i, j))
#
# linked = sum(is_visit)
# while linked < N:
#     dist, a, b = heapq.heappop(dists)
#     if find(a) != find(b):
#         answer += dist
#         union(a, b)
#         linked += 1
#
# print(format(answer, ".2f"))
