import sys
import heapq

input = sys.stdin.readline
N, M = map(int, input().split())
roads = []   # 연결된 길들을 저장할 리스트
parents = [i for i in range(N+1)]   # 각 집의 부모노드를 자기자신으로 설정한다
count = 0   # 연결된 길의 수를 0으로 초기화 한다
answer = 0


# 부모 노드를 찾는 함수
def find(n):
    parent = parents[n]   # 입력의 부모노드를 받아온다
    if parent != n:   # 부모노드가 입력과 다르다면
        parent = find(parents[n])   # 부모노드의 부모노드를 찾는다
    return parent   # 부모노드를 반환한다


# 노드를 합치는 함수
def union(A, B):
    first = find(A)   # 첫 번째 입력의 부모노드를 찾는다
    second = find(B)   # 두 번째 입력의 부모노드를 찾는다
    if first < second:   # 첫 번째의 부모노드가 더 작으면
        parents[second] = first   # 두 번째의 부모노드를 첫 번째와 같게 맞춘다
    else:   # 반대의 경우
        parents[first] = second   # 첫 번째의 부모노드를 두 번째와 같게 맞춘다


for _ in range(M):   # 길 갯수만큼
    a, b, c = list(map(int, input().split()))
    heapq.heappush(roads, (c, a, b))   # 리스트에 heap으로 넣어준다(비용 순으로 오름차순 저장)

while count != N-2:   # 마을 갯수 -2번개의 길을 연결한다
    c, a, b = heapq.heappop(roads)   # 비용이 적은 순으로 불러와
    if find(a) != find(b):   # 부모노드가 다르면
        answer += c   # 정답에 비용을 더하고
        count += 1   # 연결된 길 수를 1개 늘리고
        union(a, b)   # 두 집의 부모노드를 합친다

print(answer)
