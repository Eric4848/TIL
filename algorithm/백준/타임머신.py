import sys

input = sys.stdin.readline
N, M = map(int, input().split())
edges = []   # 간선들을 담을 리스트
answers = [float('inf')] * (N+1)   # 거리들을 ㅁ무한으로 초기화 해서 N+1개 만든다
answers[1] = 0


def bf(start):   # 벨만-포드 알고리즘
    answers[start] = 0   # 시작점 위치의 시간을 0으로 초기화 한다
    for i in range(N):   # N회동안
        for j in range(M):   # 모든 간선에 대해
            start = edges[j][0]   # 출발
            end = edges[j][1]   # 도착
            time = edges[j][2]   # 걸리는 시간
            if answers[start] != float('inf') and answers[start] + time < answers[end]:   # 출발지가 가본적이 있고, 걸리는 시간이 도착지 시간보다 적으면
                answers[end] = answers[start] + time   # 시간을 변경한다
                if i == N-1:   # 반복횟수가 노드수와 같아지는순간 작아지는 무한루프가 반드시 생기므로
                    return True   # 종료하고 진실을 반환한다
    return False   # 아닌경우 거짓을 반환한다


for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

is_roop = bf(1)   # 루프가 생기는지를 출발지점 1에대해 계산한다


if is_roop:   # 루프가 생기면
    print(-1)   # -1 출력
else:   # 그렇지 않으면
    for answer in answers[2:]:   # 나머지 노드들에 대해
        if answer == float('inf'):   # 갈 수 없다면
            print(-1)   # -1을 출력하고
        else:   # 아니면
            print(answer)   # 도착시간을 출력한다

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
# q = deque()
# q.append((1, 0))
#
# while q:
#     s, time = q.popleft()
#     if time < minimum:
#         flag = 1
#         break
#     for route in routes[s]:
#         e, t = route
#         if time + t < answers[e]:
#             answers[e] = time + t
#             q.append((e, time+t))
#
# if flag:
#     print(-1)
# else:
#     for answer in answers[2:]:
#         if answer == float('inf'):
#             print(-1)
#         else:
#             print(answer)


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
