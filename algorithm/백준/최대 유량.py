import sys
from collections import deque


# 입력 알파벳을 사용할 인덱스로 변환하는 함수
def toNum(alph):
    if ord(alph) <= ord('Z'):   # 대문자인 경우
        return ord(alph) - ord('A')   # 0~25로 지정
    else:   # 소문자인 경우
        return ord(alph) - ord('a') + 26   # 26~51로 지정


# 흘러올 수 있는 물의 양을 찾는 함수
def findMin(node):
    global minFlow   # 흐를 수 있는 가장 작은 크기
    if node == 0:   # 시작 노드인 경우
        return   # 종료

    rest = ables[prev[node]][node] - flows[prev[node]][node]   # 흘릴 수 있는 량 - 흘러간 양
    if rest < minFlow:   # 계산값이 최소보다 작다면
        minFlow = rest   # 변경
    findMin(prev[node])   # 이전 노드에 대해 dfs


# 흐른 값을 설정
def makeFlow(node):
    if node == 0:   # 시작 노드라면
        return    # 종료
    flows[prev[node]][node] += minFlow   # 이전 노드에서 현재 노드로 최소치를 더해준다
    flows[node][prev[node]] -= minFlow   # 현재 노드에서 이전 노드로 최소치를 빼준다

    makeFlow(prev[node])   # 이전 노드에 대해 dfs


input = sys.stdin.readline
N = int(input())
graph = {}
ables = [[0] * 52 for _ in range(52)]   # 흘릴 수 있는 양 초기화
flows = [[0] * 52 for _ in range(52)]   # 흘려보낸 양 초기화
answer = 0   # 정답 초기화

# dict 생성
for i in range(52):
    graph[i] = []   # 인덱스별 딕셔너리에 리스트 생성

# 입력
for _ in range(N):
    a, b, c = input().split()
    a = toNum(a)
    b = toNum(b)
    c = int(c)
    ables[a][b] += c   # 같은 위치인 경우
    ables[b][a] += c   # 병렬 이므로 더해준다
    graph[a].append(b)   # 간선정보
    graph[b].append(a)   # 저장

while True:
    prev = [-1 for _ in range(52)]   # 이전 노드 -1로 초기화
    q = deque([0])   # deque에 시작 노드 0 저장

    # bfs
    while q:
        now = q.popleft()
        if now == 25:   # 도착노드인 경우
            break   # 종료

        for nxt in graph[now]:   # 연결된 노드별로
            if 0 < (ables[now][nxt] - flows[now][nxt]) and prev[nxt] == -1:   # 흘릴 수 있는 양 - 흘러간 양이 양수이고(흘릴 수 있다면) 해당 노드에 방문하지 않았다면
                q.append(nxt)   # 큐에 추가
                prev[nxt] = now   # 해당 노드에 이전 위치를 현재로 저장

    # 종료 조건
    if prev[25] == -1:   # 도착지점에 이을 수 있는 길이 없을 때(모든 병렬 계산이 끝난 경우)
        break   # 종료

    minFlow = float('inf')   # 최소치를 무한으로 초기화
    findMin(25)   # 종료 노드부터 최소치 계산
    makeFlow(25)   # 종료 노드부터 흐른 양 설정
    answer += minFlow   # 흐른 물의 양 정답에 추가(병렬이므로)

print(answer)
