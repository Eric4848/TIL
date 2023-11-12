from collections import deque

N = int(input())
M = int(input())
roads = [list(map(int, input().split())) for _ in range(N)]
plans = list(map(int, input().split()))
answer = 'YES'


for i in range(len(plans) - 1):
    s = plans[i] - 1
    e = plans[i + 1] - 1
    chk = 0
    is_visit = [False] * N
    is_visit[s] = True
    q = deque([s])
    while q:
        now = q.popleft()
        if now == e:
            chk = 1
            break
        for to in range(len(roads[now])):
            if not is_visit[to] and roads[now][to]:
                is_visit[to] = True
    if not chk:
        answer = 'NO'
        break

print(answer)
