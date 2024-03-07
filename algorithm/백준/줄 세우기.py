import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
reqs = [0 for _ in range(N+1)]   # 필요 조건을 0으로 초기화
nxts = [[] for _ in range(N+1)]   # 후행을 담을 리스트

for _ in range(M):
    f, b = map(int, input().split())
    nxts[f].append(b)   # 후행을 선행위치에 저장
    reqs[b] += 1   # 후행의 필요 조건 + 1

# 시작지점 설정
q = deque()
for i in range(1, N+1):
    if reqs[i] == 0:   # 필요 조건이 0이면
        q.append(i)   # 큐에 추가

answer = []
while q:
    now = q.popleft()   # 수행 가능한 일
    answer.append(now)   # 정답 리스트에 추가
    for nxt in nxts[now]:   # 수행 가능한 일의 후행 일들에 대해
        reqs[nxt] -= 1   # 필요 조건 - 1
        if reqs[nxt] == 0:   # 필요 조건이 0이 되었다면
            q.append(nxt)   # 큐에 추가

print(*answer)


# 오답
# import sys
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# dp = [0] * (N+1)
# for _ in range(M):
#     f, b = map(int, input().split())
#     dp[f] -= 1
#     dp[b] = dp[f] + 1
#
# nums = [[] for _ in range(M+1)]
# for n in range(1, N+1):
#     nums[dp[n]].append(n)
#
# answer = []
# for num in nums:
#     answer += num
#
# print(*answer)
