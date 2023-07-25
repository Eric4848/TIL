# bfs 사용
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
is_visit = [False] * (N + 1)
answer = [0] * (N + 1)   # 정답을 0으로 초기화한다
matrix = [[] for _ in range(N + 1)]

for _ in range(N-1):   # 양방향 연결 그래프를 만든다
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

to_visit = deque([1])   # bfs를 진행할 deque를 출발 노드인 root(1)로 설정한다
is_visit[1] = True   # root인 1을 방문 처리한다
while to_visit:
    x = to_visit.popleft()   # 출발지점을 x로 설정한다
    for i in matrix[x]:   # x지점과 연결된 모든 노드들 중에서
        if not is_visit[i]:   # 방문한 적이 없다면
            answer[i] = x   # 해당 노드의 부모는 출발지점으로 설정하고
            to_visit.append(i)   # 해당 노드를 출발 노드리스트에 추가한다
            is_visit[i] = True   # 해당 노드를 방문처리한다


for i in range(2, N + 1):
    print(answer[i])


# 시간 초과
# import sys
# input = sys.stdin.readline
# N = int(input())
# matrix = {i: [] for i in range(N + 1)}
# for _ in range(N-1):
#     a, b = map(int, input().split())
#     matrix[a].append(b)
#     matrix[b].append(a)
# to_visit = [1]
# while to_visit:
#     visit = to_visit.pop()
#     for i in range(2, N + 1):
#         if visit in matrix[i]:
#             matrix[i] = [visit]
#             to_visit.append(i)
#
# for i in range(2, N + 1):
#     print(*matrix[i])


# 시간 초과
# import sys
# input = sys.stdin.readline
# N = int(input())
# matrix = []
# for _ in range(N-1):
#     matrix.append(list(map(int, input().split())))
# answer = {}
# to_visit = [1]
# is_visit = [False] * N
# while to_visit:
#     visit = to_visit.pop()
#     for i in range(len(matrix)):
#         if not is_visit[i]:
#             if visit in matrix[i]:
#                 for num in matrix[i]:
#                     if num != visit:
#                         answer[num] = visit
#                         to_visit.append(num)
#                         is_visit[i] = True
#                         break
#
# for i in range(2, N + 1):
#     print(answer[i])
