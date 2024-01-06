# 시간 초과
from collections import deque

N, K = map(int, input().split())
q = deque([[N]])
is_visit = {i: False for i in range(100001)}
is_visit[N] = True

while True:
    nums = q.popleft()
    now = nums[-1]
    if now == K:
        print(len(nums)-1)
        print(*nums)
        break

    if 0 <= now-1 and not is_visit[now-1]:
        q.append(nums + [now-1])
        is_visit[now-1] = True

    if now + 1 < 100001 and not is_visit[now+1]:
        q.append(nums + [now+1])
        is_visit[now+1] = True

    if now * 2 < 100001 and not is_visit[now*2]:
        q.append(nums + [now*2])
        is_visit[now*2] = True
