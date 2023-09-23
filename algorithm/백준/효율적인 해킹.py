import sys

input = sys.stdin.readline
N, M = map(int, input().split())
believe = [[] for _ in range(N+1)]
answer = [1] * (N+1)
for _ in range(M):
    A, B = map(int, input().split())
    believe[B].append(A)


def check(n):
    for nxt in believe[n]:
        if not is_visit[nxt]:
            total[0] += 1
            is_visit[nxt] = True
            check(nxt)
            is_visit[nxt] = False


for i in range(1, N+1):
    if believe[i]:
        is_visit = [False] * (N+1)
        is_visit[i] = True
        total = [1]
        check(i)
        if answer[i] < total[0]:
            answer[i] = total[0]

maximum = max(answer)
for i in range(1, N+1):
    if answer[i] == maximum:
        print(i, end=' ')



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
