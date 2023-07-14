# 다익스트라 알고리즘
# 한 노드에서부터 다른 노드들까지의 최단거리를 구하는 알고리즘
# 단방향 연결을 기본으로 함
# 거리를 무한으로 초기화한 후 자기 노드를 0으로 하고 나머지 노드들간의 거리를 비교해가며 최소를 저장
import heapq
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]   # 1번 노드부터 시작하므로 하나더 추가
distance = [float('inf')] * (N+1)   # 거리를 모두 무한으로 초기화
starts = int(input())   # 시작할 노드

for _ in range(M):
    s, e, d = map(int, input().split())   # s: 출발노드, e: 도착노드, d: 연결된 간선의 가중치
    graph[s].append((e, d))   # 거리 정보와 도착노드를 같이 입력합니다.


def dijkstra(start):
    q = []   # heap으로 저장할 탐색할 노드, 거리 리스트
    heapq.heappush(q, (0, start))   # 거리 0과 시작 위치를 저장간다.
    distance[start] = 0   # 시작 노드까지의 거리를 0으로 변경한다

    while q:
        dist, now = heapq.heappop(q)   # 탐색할 리스트에서 거리와 현재 노드를 pop해서 불러온다

        if distance[now] < dist:   # 현재 노드까지의 거리가 현재 저장된 거리보다 멀다면
            continue   # 다음으로 넘어간다.

        for i in graph[now]:   # 현재 노드에 연결된 모든 노드
            if dist+i[1] < distance[i[0]]:   # 기존에 입력되어있는 거리보다 작다면
                distance[i[0]] = dist+i[1]   # 거리를 재설정 하고
                heapq.heappush(q, (dist+i[1], i[0]))   # 재설정한 거리와 도착 노드를 탐색할 리스트에 추가한다


dijkstra(starts)
print(distance)
