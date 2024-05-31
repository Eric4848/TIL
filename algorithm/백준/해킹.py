import sys
import heapq

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    depends = [[] for _ in range(n+1)]   # 종속되는 컴퓨터를 담을 리스트
    times = [float('inf')] * (n+1)   # 해당 컴퓨터의 감염까지 걸린 시간 무한으로 초기화
    times[c] = 0   # 첫 감염 컴퓨터 시간 변경
    q = []   # 감염될 컴퓨터를 담을 리스트 초기화
    heapq.heappush(q, (0, c))   # 리스트를 힙으로 만들어 시간 0과 시작 컴퓨터 저장
    # 종속 여부 저장
    for _ in range(d):
        a, b, s = map(int, input().split())
        depends[b].append([a, s])
    # 종속된 컴퓨터 감염 계산
    while q:
        time, now = heapq.heappop(q)   # 걸린 시간, 현재 컴퓨터
        if depends[now]:   # 현재 컴퓨터와 종속된 컴퓨터가 있다면
            for nxt, t in depends[now]:   # 컴퓨터와 감염된 시간별로
                if time + t < times[nxt]:   # 현재 시간보다 새로운 감염시간이 짧다면
                    times[nxt] = time + t   # 시간을 변경하고
                    heapq.heappush(q, (time+t, nxt))   # 변경한 시간과 해당 컴퓨터를 힙에 저장
    cnt = 0   # 감염된 컴퓨터 갯수
    time = 0   # 총 시간
    for i in range(1, n+1):   # 각 컴퓨터별로
        if times[i] != float('inf'):   # 시간이 무한이 아니라면(감염되었다면)
            cnt += 1   # 갯수 1 증가
            time = max(time, times[i])   # 현재 총 시간과 해당 컴퓨터의 시간 중 큰 것 저장
    print(cnt, time)


# 시간 초과
# import sys
# from collections import deque
#
# input = sys.stdin.readline
# T = int(input())
# for _ in range(T):
#     n, d, c = map(int, input().split())
#     depends = [[] for _ in range(n+1)]
#     times = [0] * (n+1)
#     q = deque([(c, 0)])
#     for _ in range(d):
#         a, b, s = map(int, input().split())
#         depends[b].append([a, s])
#     while q:
#         now, time = q.popleft()
#         if depends[now]:
#             for nxt, t in depends[now]:
#                 if not times[nxt]:
#                     times[nxt] = time + t
#                     q.append((nxt, time+t))
#                 else:
#                     if time + t < times[nxt]:
#                         times[nxt] = time + t
#                         q.append((nxt, time+t))
#     cnt = 1
#     for time in times:
#         if time:
#             cnt += 1
#     print(cnt, max(times))
