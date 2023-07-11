import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
starts = []
ends = []
costs = []
answer = [float('inf')]
is_used = [False] * M
for _ in range(M):
    s, e, c = map(int, input().split())
    starts.append(s)
    ends.append(e)
    costs.append(c)
start, end = map(int, input().split())


print(answer[0])

# 시간 초과
# import sys
# sys.setrecursionlimit(10**8)
# input = sys.stdin.readline
#
# N = int(input())
# M = int(input())
# starts = []
# ends = []
# costs = []
# answer = [float('inf')]
# is_used = [False] * M
# for _ in range(M):
#     s, e, c = map(int, input().split())
#     starts.append(s)
#     ends.append(e)
#     costs.append(c)
# start, end = map(int, input().split())
#
#
# def search(f, t, counts):
#     if f == t:
#         if counts < answer[0]:
#             answer[0] = counts
#         return
#     for i in range(M):
#         if not is_used[i]:
#             if starts[i] == f:
#                 is_used[i] = True
#                 search(ends[i], t, counts + costs[i])
#                 is_used[i] = False
#
#
# search(start, end, 0)
# print(answer[0])
