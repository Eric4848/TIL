# 시간 초과
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
m = int(input())
bus = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    bus[a].append((b, c))
answers = [[float('inf')] * (n+1) for _ in range(n+1)]

for starts in range(1, n+1):
    answers[starts][starts] = 0
    q = deque()
    q.append(starts)
    while q:
        s = q.popleft()
        for e, l in bus[s]:
            if answers[starts][s] + l < answers[starts][e]:
                q.append(e)
                answers[starts][e] = answers[starts][s] + l
    for i in range(1, n+1):
        if answers[starts][i] == float('inf'):
            answers[starts][i] = 0

for i in range(1, n+1):
    print(*answers[i][1:])


# 시간 초과
# from collections import deque
#
# n = int(input())
# m = int(input())
# bus = [[] for _ in range(n+1)]
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     bus[a].append((b, c))
# answers = [[float('inf')] * (n+1) for _ in range(n+1)]
#
# for starts in range(1, n+1):
#     answers[starts][starts] = 0
#     q = deque()
#     q.append(starts)
#     while q:
#         s = q.popleft()
#         for e, l in bus[s]:
#             if answers[starts][s] + l < answers[starts][e]:
#                 q.append(e)
#                 answers[starts][e] = answers[starts][s] + l
#
# for i in range(1, n+1):
#     print(*answers[i][1:])
