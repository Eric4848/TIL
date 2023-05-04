from collections import deque

S, E = map(int, input().split())
lists = deque()
lists.append(S)
is_visit = [False for _ in range(100001)]
is_visit[S] = True
answer = 0

while E not in lists:
    for _ in range(len(lists)):
        nxt = lists.popleft()
        if nxt < 100000:
            if not is_visit[nxt + 1]:
                lists.append(nxt + 1)
                is_visit[nxt + 1] = True

        if nxt > 0:
            if not is_visit[nxt - 1]:
                lists.append(nxt - 1)
                is_visit[nxt - 1] = True

        if nxt * 2 < 100001:
            if not is_visit[nxt * 2]:
                lists.append(nxt * 2)
                is_visit[nxt * 2] = True

    answer += 1

print(answer)


# from collections import deque
#
# S, E = map(int, input().split())
# lists = deque()
# lists.append(S)
# visits = [0] * 100001
#
# while True:
#     now = lists.popleft()
#     if now == E:
#         print(visits[now])
#         break
#
#     for nxt in (now+1, now-1, now*2):
#         if 0 <= nxt < 100001 and not visits[nxt]:
#             visits[nxt] = visits[now] + 1
#             lists.append(nxt)
