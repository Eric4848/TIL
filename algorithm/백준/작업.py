import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
times = [0]   # 작업 시간을 담을 리스트
nxts = [[] for _ in range(N+1)]   # 다음에 수행할 작업을 담을 리스트
reqs = [0 for _ in range(N+1)]   # 필요한 작업들의 수
dp = [0 for _ in range(N+1)]   # 총 필요시간을 초기화
q = deque([])

for i in range(N):
    nums = list(map(int, input().split()))
    times.append(nums[0])   # 작업시간 저장
    if nums[1] == 0:   # 필요 작업이 없는경우
        q.append(i+1)   # 큐에 추가
        dp[i+1] = nums[0]   # 해당 작업 필요시간 설정
    else:   # 필요 작업이 있는 경우
        reqs[i+1] = nums[1]   # 필요 작업 수 저장
        for j in range(nums[1]):   # 필요 작업 수 만큼
            nxts[nums[j+2]].append(i+1)   # 필요한 작업에 다음 작업을 저장

while q:
    now = q.popleft()
    for nxt in nxts[now]:   # 현재 작업 후 진행할 작업들에 대해
        reqs[nxt] -= 1   # 필요 작업수 -1
        dp[nxt] = max(dp[nxt], times[nxt] + dp[now])   # 해당 작업에 필요한 시간을 원래 값과 현재까지 시간 + 다음 작업시간 중 큰 것으로 변경
        if reqs[nxt] == 0:   # 필요 작업을 모두 한 경우
            q.append(nxt)   # 큐에 추가

print(max(dp))
