import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
times = [0 for _ in range(N+1)]
nxts = [[] for _ in range(N+1)]
reqs = [0 for _ in range(N+1)]
answers = [0 for _ in range(N+1)]
q = deque()

# 정보 입력
for i in range(1, N+1):
    specs = list(map(int, input().split()))
    times[i] = specs[0]   # 걸리는 시간 저장
    # 필요 조건 계산
    idx = 1
    while True:
        # 마지막 요소면 종료
        if specs[idx] == -1:
            break

        # 필요 조건 추가
        reqs[i] += 1   # 필요 조건 + 1
        nxts[specs[idx]].append(i)   # 필요한 요소의 다음으로 현재 추가
        idx += 1

    # 초기 설정
    if reqs[i] == 0:   # 필요 조건이 없으면
        q.append(i)   # 큐에 추가하고
        answers[i] = times[i]   # 정답에 해당 건물 건설 시간 저장

# 건물 시간 계산
while q:
    now = q.popleft()
    for nxt in nxts[now]:   # 다음으로 이어지는 건물들별로
        reqs[nxt] -= 1   # 요구치 - 1
        answers[nxt] = max(answers[nxt], answers[now] + times[nxt])   # 총 걸린 시간을 저장된 값과 이전 + 현재 짓는 시간 중 큰것으로 저장
        if reqs[nxt] == 0:   # 요구치를 모두 만족한 경우
            q.append(nxt)   # 큐에 추가

for i in range(1, N+1):
    print(answers[i])
