import sys
import heapq

input = sys.stdin.readline
n = int(input())
m = int(input())
roads = [[] for _ in range(n+1)]   # 길을 저장할 리스트
routes = [[] for _ in range(n+1)]   # 해당 위치까지 가는 경로를 저장할 리스트
times = [float('inf') for _ in range(n+1)]   # 해당 위치까지 걸린 시간을 무한으로 초기화

# 길들을 저장
for _ in range(m):
    d, a, t = map(int, input().split())
    roads[d].append((t, a))   # 출발지에 시간, 도착지 순으로 저장(heap을 사용할 예정이므로 시간 먼저)

s, e = map(int, input().split())
times[s] = 0   # 시작지점까지 걸린 시간 0
q = []   # heap을 담을 큐
routes[s].append(s)   # 시작 경로 정보에 시작위치 추가
heapq.heappush(q, (0, s))   # heap에 총 걸린시간 0, 현재 위치 s추가
while q:
    time, now = heapq.heappop(q)   # 현재까지 걸린 시간, 현재 위치
    if times[now] < time:   # 현재까지 걸린 시간이 현재 위치까지 가는 시간보다 크면
        continue   # 넘어간다

    for nt, nxt in roads[now]:   # 현재 위치와 이어진 길별로
        newtime = time + nt   # 다음 지역까지 걸린 시간
        if newtime < times[nxt]:   # 다음 지역까지 걸린 시간이 이전 값보다 작으면
            heapq.heappush(q, (newtime, nxt))   # 큐에 걸린 시간, 다음 지역 추가
            times[nxt] = newtime   # 다음 지역까지 걸린 시간 갱신
            routes[nxt] = routes[now][:] + [nxt]   # 다음 지역까지 걸린 경로를 현재까지 경로 + 다음 위치로 갱신

print(times[e])
print(len(routes[e]))
print(*routes[e])
