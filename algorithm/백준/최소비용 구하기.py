# 다익스트라 dijkstra => 노드간 최소거리 구할 때 사용
import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]   # N까지 다리들을 저장할 graph
times = [float('inf')] * (N + 1)   # N까지 걸린 시간을 저장할 times
for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((c, e))   # 시작 지점인덱스 graph에 걸리는 시간과 도착지점 저장
start, end = map(int, input().split())


def dijkstra(x):
    pq = []   # 연결 된 노드들을 저장해 둘 리스트
    heapq.heappush(pq, (0, x))   # 시간 0, 위치 start인 노드 추가
    times[x] = 0   # start까지 걸린 시간을 0으로 변경
    while pq:
        time, x = heapq.heappop(pq)   # 걸리는 시간, 도착지를 time, x로 받아와서
        if times[x] < time:   # 그 지점까지 걸리는 시간보다 받아온 시간이 더 오래걸리면
            continue   # 넘어간다
        for nt, nx in graph[x]:   # 아닌경우 x지점의 다리의 시간과 도착지를 불러와서
            newtime = time + nt   # 새로 걸린 시간을 현 지점까지 걸린 시간과 그 지점까지 걸릴 시간의 합을 구한다
            if times[nx] > newtime:   # 구한 시간이 도착지까지 걸린 시간보다 짧다면
                heapq.heappush(pq, (newtime, nx))   # 그 지점에서부터의 다리를 새로 추가하고
                times[nx] = newtime   # 그 지점까지 걸린 시간 재설정 해준다


dijkstra(start)   # 함수에 시작점을 넣어 실행하고

print(times[end])   # 도착점의 시간을 출력한다

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
