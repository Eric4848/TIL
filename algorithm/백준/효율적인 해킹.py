import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
believe = [[] for _ in range(N+1)]
answer = [1] * (N+1)
maximum = 0
for _ in range(M):
    A, B = map(int, input().split())
    believe[B].append(A)


def bfs(n):
    q = deque()
    q.append(believe[i])
    while q:
        now = q.popleft()
        for nxt in now:
            if not is_visit[nxt]:
                is_visit[nxt] = True
                answer[n] += 1
                q.append(believe[nxt])


for i in range(1, N+1):
    is_visit = [False] * (N+1)
    bfs(i)
    if maximum < answer[i]:
        maximum = answer[i]

for i in range(1, N+1):
    if answer[i] == maximum:
        print(i, end=' ')


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# believe = [[] for _ in range(N+1)]
# answer = [1] * (N+1)
# maximum = 0
# for _ in range(M):
#     A, B = map(int, input().split())
#     believe[B].append(A)
#
#
# def add(n):
#     for nxt in believe[n]:
#         if answer[nxt] == 1:
#             add(nxt)
#         answer[i] += answer[nxt]
#
#
# for i in range(1, N+1):
#     add(i)
#     if maximum < answer[i]:
#         maximum = answer[i]
#
# for i in range(1, N+1):
#     if answer[i] == maximum:
#         print(i, end=' ')


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# believe = [[] for _ in range(N+1)]
# answer = [1] * (N+1)
# for _ in range(M):
#     A, B = map(int, input().split())
#     believe[B].append(A)
#
#
# def add(n, f):
#     for nxt in believe[n]:
#         add(nxt, f)
#         answer[f] += 1
#
#
# for i in range(1, N+1):
#     add(i, i)
#
# maximum = max(answer)
# for i in range(1, N+1):
#     if answer[i] == maximum:
#         print(i, end=' ')


# 시간 초과
# N, M = map(int, input().split())
# believe = [[] for _ in range(N+1)]
# answer = [1] * (N+1)
# for _ in range(M):
#     A, B = map(int, input().split())
#     believe[B].append(A)
#
#
# def check(n):
#     for nxt in believe[n]:
#         if not is_visit[nxt]:
#             total[0] += 1
#             is_visit[nxt] = True
#             check(nxt)
#             is_visit[nxt] = False
#
#
# for i in range(1, N+1):
#     if believe[i]:
#         is_visit = [False] * (N+1)
#         is_visit[i] = True
#         total = [1]
#         check(i)
#         if answer[i] < total[0]:
#             answer[i] = total[0]
#
# maximum = max(answer)
# answerp = []
# for i in range(1, N+1):
#     if answer[i] == maximum:
#         answerp.append(i)
# print(*answerp)
