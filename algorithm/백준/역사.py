# 시간 초과
# import sys
#
# input = sys.stdin.readline
# n, k = map(int, input().split())
# nxts = [[0] * (n+1) for _ in range(n + 1)]
# for _ in range(k):
#     a, b = map(int, input().split())
#     nxts[a][b] = -1
#     nxts[b][a] = 1
#
# for k in range(n+1):
#     for i in range(n+1):
#         for j in range(n+1):
#             if nxts[i][k] and nxts[i][k] == nxts[k][j]:
#                 nxts[i][j] = nxts[i][k]
#
# s = int(input())
# for _ in range(s):
#     s, e = map(int, input().split())
#     if nxts[s][e]:
#         print(nxts[s][e])
#     else:
#         print(0)


# 시간 초과
# Pypy 제출
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
nxts = [[0] * (n+1) for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    nxts[a][b] = 1

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if nxts[i][k] and nxts[k][j]:
                nxts[i][j] = 1

s = int(input())
for _ in range(s):
    s, e = map(int, input().split())
    if nxts[s][e]:
        print(-1)
    elif nxts[e][s]:
        print(1)
    else:
        print(0)


# n, k = map(int, input().split())
# nxts = [[] for _ in range(n + 1)]
# for _ in range(k):
#     a, b = map(int, input().split())
#     nxts[a].append(b)
#
# s = int(input())
# for _ in range(s):
#     s, e = map(int, input().split())
