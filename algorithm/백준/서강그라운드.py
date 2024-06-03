import sys
import heapq

input = sys.stdin.readline
n, m, r = map(int, input().split())
items = list(map(int, input().split()))   # 지역별 아이템 수 저장
roads = [[] for _ in range(n)]   # 지역별 연결 지역을 저장할 리스트
answer = 0   # 정답 초기화
# 이어진 길 저장
for _ in range(r):
    a, b, l = map(int, input().split())
    roads[a-1].append([l, b-1])   # 양쪽 모두에
    roads[b-1].append([l, a-1])   # 추가
# 시작 지역별 계산
for s in range(n):
    dists = [float('inf')] * n   # 거리를 무한으로 초기화
    dists[s] = 0   # 시작지점 거리를 0으로 초기화
    q = []   # 도달 가능지역을 힙으로 저장할 리스트
    heapq.heappush(q, [0, s])   # 힙에 거리 0, 시작지점 저장
    # 계산
    while q:
        d, now = heapq.heappop(q)   # 거리, 현재위치를 가져온다
        for l, nxt in roads[now]:   # 현재 위치에서 이어진 길별로
            if d + l <= m and d + l < dists[nxt]:   # 제한조건 이내, 저장된 거리보다 작으면
                heapq.heappush(q, [d+l, nxt])   # 힙에 추가
                dists[nxt] = d + l   # 거리 변경
    total = 0   # 총 아이템수 초기화
    for i, dist in enumerate(dists):   # 거리별로
        if dist != float('inf'):   # 도달 가능한 거리면
            total += items[i]   # 해당 지역 아이템 추가
    answer = max(answer, total)   # 정답과 비교하여 큰 것 저장
print(answer)
