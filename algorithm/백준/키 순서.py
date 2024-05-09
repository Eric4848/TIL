# 시간 초과
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
taller = [[] for _ in range(N+1)]
cnts = [[False] * (N+1) for _ in range(N+1)]
answer = 0

for _ in range(M):
    a, b = map(int, input().split())
    taller[a].append(b)

for i in range(1, N+1):
    q = taller[i][:]
    while q:
        now = q.pop()
        cnts[i][now] = True
        cnts[now][i] = True
        for nxt in taller[now]:
            q.append(nxt)

for cnt in cnts:
    if sum(cnt) == N-1:
        answer += 1

print(answer)


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# taller = [[] for _ in range(N+1)]
# smaller = [[] for _ in range(N+1)]
# answer = 0
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     taller[b].append(a)
#     smaller[a].append(b)
#
# for i in range(1, N+1):
#     is_chk = [False] * (N + 1)
#     tall = taller[i][:]
#     while tall:
#         now = tall.pop()
#         is_chk[now] = True
#         for nxt in taller[now]:
#             tall.append(nxt)
#     small = smaller[i][:]
#     while small:
#         now = small.pop()
#         is_chk[now] = True
#         for nxt in smaller[now]:
#             small.append(nxt)
#
#     if sum(is_chk) == N-1:
#         answer += 1
#
# print(answer)
