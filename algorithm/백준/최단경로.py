import heapq   # 힙과
import sys
input = sys.stdin.readline   # readline을 사용해야 시간초과가 나지 않는다

V, E = map(int, input().split())
S = int(input())
lines = [[] for _ in range(V + 1)]   # 정점별 간선을 담을 리스트를 V+1개 만들어준다
answers = [float('inf')] * (V+1)   # 정점별 이동 거리를 무한으로 초기화 해 V+1개 만들어준다
answers[S] = 0   # 시작점의 거리를 0으로 변경한다

for _ in range(E):   # 간선들을 리스트에 저장한다
    u, v, w = map(int, input().split())
    lines[u].append((v, w))

q = []   # 힙으로 쓸 리스트
heapq.heappush(q, (0, S))   # 힙에 현재까지 이동한 거리와 출발점을 저장한다

while q:
    d, now = heapq.heappop(q)   # 이동거리 d와 현재 위치를 불러온다

    if answers[now] < d:   # 현재위치까지 걸린 거리보다 이동거리가 길면
        continue   # 넘어간다

    for nxt in lines[now]:   # 현재 위치와 연결된 간선별로
        if d + nxt[1] < answers[nxt[0]]:   # 간선의 도착지점까지의 거리보다 현재까지 거리 + 도착지점까지 거리가 작다면
            answers[nxt[0]] = d + nxt[1]   # 도착지점의 이동거리를 변경하고
            heapq.heappush(q, (d + nxt[1], nxt[0]))   # 도착지점의 이동거리와 도착지점을 힙에 추가한다

for i in range(1, V+1):   # 각 정점별로
    if answers[i] == float('inf'):   # 무한이면
        print('INF')   # 무한을
    else:   # 아니면
        print(answers[i])   # 이동거리를 출력한다


# 시간초과
# import sys
# input = sys.stdin.readline
#
# V, E = map(int, input().split())
# S = int(input())
# lines = {i: []for i in range(V + 1)}
# answers = [float('inf')] * (V+1)
# answers[S] = 0
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     lines[u].append((v, w))
# q = [(0, S)]
# while q:
#     d, now = q.pop()
#
#     if answers[now] < d:
#         continue
#
#     for i in lines[now]:
#         if d + i[1] < answers[i[0]]:
#             answers[i[0]] = d + i[1]
#             q.append((d+i[1], i[0]))
#
# for i in range(1, V+1):
#     if answers[i] == float('inf'):
#         print('INF')
#     else:
#         print(answers[i])
