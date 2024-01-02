import sys
import heapq

input = sys.stdin.readline
N = int(input())
edges = [[] for _ in range(N+1)]
answers = []
for _ in range(N-1):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))


def count(n):
    childs = edges[n]
    if not childs:
        return 0

    else:
        tmp = []
        for child in childs:
            heapq.heappush(tmp, -child[1] + count(child[0]))

        if len(childs) == 1:
            heapq.heappush(answers, tmp[0])

        else:
            heapq.heappush(answers, tmp[0] + tmp[1])

        return tmp[0]


count(1)
print(-answers[0])


# 가장 깊은 경우만 계산
# import sys
#
# input = sys.stdin.readline
# N = int(input())
# edges = [[] for _ in range(N+1)]
# answers = []
# for _ in range(N-1):
#     a, b, c = map(int, input().split())
#     edges[a].append((b, c))
#
#
# def count(n, d, total):
#     childs = edges[n]
#     if not childs:
#         answers.append((d, total))
#         return
#     for child in childs:
#         count(child[0], d + 1, total + child[1])
#
#
# print(edges)
# count(edges[1][0][0], 0, edges[1][0][1])
# print(answers)
# answers = []
# count(edges[1][1][0], 0, edges[1][1][1])
# print(answers)
