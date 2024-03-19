# Union-Find
import sys
import heapq   # 다리의 하중이 큰 순서대로 계산하므로 heap사용

input = sys.stdin.readline
N, M = map(int, input().split())
bridges = []   # 다리들을 담을 리스트


# 부모 노드를 찾는 함수
def find(c):
    if parents[c] == c:   # 부모 노드가 자기 자신이면
        return c   # 자신 반환
    parents[c] = find(parents[c])   # 자신의 부모 노드를 갱신한다
    return parents[c]   # 자신의 부모 노드 반환


# 부모 노드를 합치는 함수
def union(a, b):
    # 두 노드의 부모노드를 찾아
    A = find(a)
    B = find(b)
    # 더 작은 부모 노드로 통일시킨다
    if A < B:
        parents[B] = parents[A]
    else:
        parents[A] = parents[B]


# 둘의 부모노드가 같은지 확인(이동 가능)
def check(a, b):
    return find(a) == find(b)


parents = [i for i in range(N+1)]   # 부모노드를 자신으로 초기화
# 다리 정보 입력
for _ in range(M):
    a, b, w = map(int, input().split())   # 두 지점과 무게를 입력받는다
    heapq.heappush(bridges, (-w, a, b))   # heap에 무게를 음수로 하여(제한 무게가 큰 것부터 계산하기 위해) 저장한다

s, e = map(int, input().split())   # 출발, 도착 지점

# 최대 하중 계산
while bridges:   # 다리 만큼
    w, a, b = heapq.heappop(bridges)   # 거리, 두 지점을 pop한다
    w = -w   # 무게에 -1을 곱하여 양수로 바꾼다
    union(a, b)   # 두 지점을 연결한다
    if check(s, e):   # 출발, 도착지점이 연결되었으면
        print(w)   # 현재 무게 출력
        break   # 종료


# 메모리 초과
# import sys
# import heapq
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# bridges = [[0 for i in range(N+1)] for _ in range(N+1)]
# weights = [0 for _ in range(N+1)]
# answer = 0
# for _ in range(M):
#     a, b, d = map(int, input().split())
#     bridges[a][b] = max(bridges[a][b], d)
#     bridges[b][a] = max(bridges[b][a], d)
#
# s, e = map(int, input().split())
# heap = []
# heapq.heappush(heap, (-float('inf'), s))
# while heap:
#     weight, now = heapq.heappop(heap)
#
#     if now == e:
#         break
#
#     weight = -weight
#
#     for nxt in range(1, N+1):
#         if bridges[now][nxt]:
#             newweight = min(weight, bridges[now][nxt])
#             if weights[nxt] < newweight:
#                 weights[nxt] = newweight
#                 heapq.heappush(heap, (-newweight, nxt))
#
# print(weights[e])


# 시간 초과
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# bridges = {i: [] for i in range(N+1)}
# weights = [0 for _ in range(N+1)]
# answer = 0
# for _ in range(M):
#     a, b, d = map(int, input().split())
#     bridges[a].append((b, d))
#     bridges[b].append((a, d))
#
# s, e = map(int, input().split())
# bridges[e] = []
# q = deque([(s, float('inf'))])
# while q:
#     now, weight = q.popleft()
#     for nxt, nxtweight in bridges[now]:
#         newweight = min(weight, nxtweight)
#         if weights[nxt] < newweight:
#             weights[nxt] = newweight
#             q.append((nxt, newweight))
#
# print(weights[e])


# 시간 초과
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# bridges = [[] for _ in range(N+1)]
# weights = [0 for _ in range(N+1)]
# answer = 0
# for _ in range(M):
#     a, b, d = map(int, input().split())
#     bridges[a].append((b, d))
#     bridges[b].append((a, d))
#
# s, e = map(int, input().split())
# q = deque([(s, float('inf'))])
# while q:
#     now, weight = q.popleft()
#
#     if now == e:
#         continue
#
#     for nxt, nxtweight in bridges[now]:
#         newweight = min(weight, nxtweight)
#         if weights[nxt] < newweight:
#             weights[nxt] = newweight
#             q.append((nxt, newweight))
#
# print(weights[e])
