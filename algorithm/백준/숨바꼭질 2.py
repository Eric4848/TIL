# 시간 초과
from collections import deque

N, K = map(int, input().split())
is_visit = [False] * 100001
is_visit[N] = True
q = deque([[N, 0]])
answers = [100000, 0]
while q:
    now, count = q.popleft()
    if answers[0] < count:
        break
    if now == K:
        answers[0] = count
        answers[1] += 1
        continue

    if 0 < now:
        if not is_visit[now-1]:
            q.append([now-1, count+1])
    if now < 100000:
        if not is_visit[now+1]:
            q.append([now+1, count+1])

    if now <= 50000:
        if not is_visit[now*2]:
            q.append([now*2, count+1])
print(*answers)
