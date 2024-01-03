import sys

sys.setrecursionlimit(10 ** 6)
N = int(input())
childs = [[] for i in range(N+1)]   # 자식들과 거리를 저장할 리스트
answer = 0   # 정답을 0으로 초기화

for i in range(N - 1):   # N-1개(N개의 노드끼리 연결이라 -1)
    a, b, c = map(int, input().split())
    childs[a].append((b, c))


# 계산하는 함수
def count(n):
    global answer   # 정답을 전역변수화
    max1 = max2 = 0   # 자식들의 합 최대치 2개를 0으로 초기화
    for nxt, cost in childs[n]:   # 해당 노드의 자식노드별로
        temp = count(nxt) + cost   # 다음 노드의 최대합의 값과 다음 노드까지의 거리를 더한 값을 임시값으로 저장한다
        if temp >= max1:   # 임시값이 가장 큰 값보다 크거나 같다면(같은 크기가 2개인 경우 계산)
            max1, max2 = temp, max1   # 기존 가장 큰 값을 두 번째로 큰 값으로 바꾸고 임시값을 가장 큰 값으로 저장
        elif temp > max2:   # 가장 큰값보단 작고 두 번째로 큰 값보다 크다면
            max2 = temp   # 두 번째로 큰 값을 저장
    answer = max(answer, max1 + max2)   # 정답을 두 하위노드의 합과 정답 중 큰 것으로 저장
    return max1   # 가장 큰 값을 반환


count(1)
print(answer)


# 오답
# import sys
# import heapq
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
# def count(n):
#     childs = edges[n]
#     if not childs:
#         return 0
#
#     else:
#         tmp = []
#         for child in childs:
#             heapq.heappush(tmp, -child[1] + count(child[0]))
#
#         if len(childs) == 1:
#             heapq.heappush(answers, tmp[0])
#
#         else:
#             heapq.heappush(answers, tmp[0] + tmp[1])
#
#         return tmp[0]
#
#
# count(1)
# print(-answers[0])


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
