import sys
import heapq


# 부모 노드를 찾는 함수
def find(n):
    parent = parents[n]
    if parent != n:
        parent = find(parent)
    return parent


# 두 노드의 부모노드를 합치는 함수
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


input = sys.stdin.readline
N = int(input())
locs = [list(map(float, input().split())) for _ in range(N)]   # 별들의 위치를 float형으로 저장
dists = []   # 별들의 거리와 위치를 힙으로 저장할 리스트
parents = [i for i in range(N)]   # 부모 노드를 자신으로 초기화
cnt = 0   # 연결한 횟수 초기화
answer = 0   # 비용을 초기화
# 두 지점별 거리 저장
for s in range(N-1):   # 시작 지점
    for e in range(s+1, N):   # 도착 지점
        x1, y1 = locs[s]   # 시작 좌표
        x2, y2 = locs[e]   # 도착 좌표
        # 거리 계산 -> x, y 좌표의 rms 값을 2째자리까지 계산
        d = round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 2)
        heapq.heappush(dists, (d, s, e))   # 리스트에 거리, 두 위치번호 저장
# 연결 계산
while cnt < N - 1:   # 갯수 - 1번 연결
    d, a, b = heapq.heappop(dists)   # 거리와 두 위치를 힙에서 가져오기
    if find(a) != find(b):   # 두 위치의 부모가 다르면
        union(a, b)   # 부모를 합친다
        cnt += 1   # 연결 횟수를 늘린다
        answer += d   # 정답에 거리를 더한다

print(answer)
