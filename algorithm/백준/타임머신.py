import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
answers = [float('inf')] * (N+1)
answers[1] = 0
routes = [[] for _ in range(N+1)]
minimum = 0
flag = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    routes[A].append((B, C))
    if C < 0:
        minimum += C
q = deque([1])

while q:
    s = q.popleft()
    if answers[s] < minimum:
        flag = 1
        break
    for route in routes[s]:
        e, t = route
        if answers[s] + t < answers[e]:
            answers[e] = answers[s] + t
            q.append(e)

if flag:
    print(-1)
else:
    for answer in answers[2:]:
        if answer == float('inf'):
            print(-1)
        else:
            print(answer)


# 시간 초과
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# answers = [float('inf')] * (N+1)
# answers[1] = 0
# routes = [[] for _ in range(N+1)]
# minimum = 0
# flag = 0
#
# for _ in range(M):
#     A, B, C = map(int, input().split())
#     routes[A].append((B, C))
#     if C < 0:
#         minimum += C
# q = deque([1])
#
# while q:
#     s = q.popleft()
#     if answers[s] < minimum:
#         flag = 1
#         break
#     for route in routes[s]:
#         e, t = route
#         if answers[s] + t < answers[e]:
#             answers[e] = answers[s] + t
#             q.append(e)
#
# if flag:
#     print(-1)
# else:
#     for answer in answers[2:]:
#         if answer == float('inf'):
#             print(-1)
#         else:
#             print(answer)
