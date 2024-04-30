import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
reqs = [0 for _ in range(N+1)]   # 앞순서 인원을 0으로 초기화
nxts = [[] for _ in range(N+1)]   # 뒷순서 인원을 빈 리스트로 초기화
q = deque([])
answers = []   # 정답을 담을 리스트
# 각 담당 출연 순서 저장
for _ in range(M):
    orders = list(map(int, input().split()))   # 순서를 입력받음
    for i in range(1, orders[0]):   # 1번순서 ~ 뒤에서 두번째 까지
        nxts[orders[i]].append(orders[i+1])   # 현 가수 뒷 순서로 다음 가수를 저장
        reqs[orders[i+1]] += 1   # 다음 가수의 앞순서 인원 + 1

# 출연 가능한 가수들 큐에 저장
for i in range(1, N+1):
    if not reqs[i]:   # 앞순서가 없는 가수들을
        q.append(i)   # 큐에 저장

# 무대 순서 정하기
while q:
    now = q.popleft()   # 순서에 맞는 가수 리스트에서 popleft
    answers.append(now)   # 정답에 해당 가수 저장
    for nxt in nxts[now]:   # 그 가수 다음 가수별로
        reqs[nxt] -= 1   # 앞순서 -1
        if not reqs[nxt]:   # 앞순서가 없는 경우
            q.append(nxt)   # 출연 가능 리스트에 추가

# 가, 불가 판별
if len(answers) == N:   # 가수 리스트에 모든 인원이 있다면
    for answer in answers:   # 가수별로
        print(answer)   # 출력
else:   # 인원이 부족하다면
    print(0)   # 0 출력
