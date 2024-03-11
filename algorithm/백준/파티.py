import sys
from collections import deque

input = sys.stdin.readline
N, M, X = map(int, input().split())
froads = [[] for _ in range(N+1)]   # 가는 길을 저장할 리스트
broads = [[] for _ in range(N+1)]   # 오는 길을 저장할 리스트
answers = [[float('inf') for _ in range(N+1)] for _ in range(2)]   # 가는시간, 오는시간을 무한으로 초기화

# 가는 길, 오는 길 저장
for _ in range(M):
    s, e, t = map(int, input().split())
    froads[e].append((s, t))   # 가는 길 저장(도착지점 기준으로 저장)
    broads[s].append((e, t))   # 오는 길 저장(출발지점 기준으로 저장)

# 가는 시간 계산
q = deque([X])   # deque에 목적지 저장
answers[0][X] = 0   # 목적지까지 걸린 시간 0으로 초기화
while q:   # bfs
    now = q.popleft()   # 현재 위치
    for nxt, time in froads[now]:   # 현재 위치와 이어진 길과 시간으로
        if answers[0][now] + time < answers[0][nxt]:   # 현위치에서 이동하는게 도착지까지의 시간보다 빠르면
            answers[0][nxt] = answers[0][now] + time   # 도착시간 변경
            q.append(nxt)   # 도착지를 큐에 추가

# 오는 시간 계산(가는 시간과 동일)
q = deque([X])
answers[1][X] = 0
while q:
    now = q.popleft()
    for nxt, time in broads[now]:
        if answers[1][now] + time < answers[1][nxt]:
            answers[1][nxt] = answers[1][now] + time
            q.append(nxt)

# 정답 계산
answer = 0   # 정답을 0으로 초기화
for i in range(1, N+1):   # 각 사람별로
    answer = max(answer, answers[0][i] + answers[1][i])   # 저장된 값과 가는시간+오는시간 중 큰 것 저장

print(answer)
