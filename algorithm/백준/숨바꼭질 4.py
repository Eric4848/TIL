from collections import deque


# 지나온 길을 찾아 출력하는 함수
def path(x):
    arr = []   # 지나온 길을 담을 리스트
    latest = x   # 가장 최근 지나온 길
    for _ in range(dist[x] + 1):   # 이동 횟수 + 1번
        arr.append(latest)   # 마지막 위치를 저장하고
        latest = befores[latest]   # 마지막 위치를 그 전으로 변경한다
    print(' '.join(map(str, arr[::-1])))   # 역순으로 문자열로 바꿔 출력한다


# 길을 찾는 함수
def bfs():
    q = deque()
    q.append(N)
    while q:
        now = q.popleft()
        if now == K:   # 현재 위치가 도착지면
            print(dist[now])   # 도착지까지 거리를 출력
            path(now)   # 길을 찾아 출력하는 함수 실행
            return
        for nxt in (now + 1, now - 1, 2 * now):   # 3가지 방법 중
            if 0 <= nxt < 100001 and not dist[nxt]:   # 범위 이내고 방문한 적이 없는 곳이면
                q.append(nxt)   # 다음 위치를 큐에 추가
                dist[nxt] = dist[now] + 1   # 이동 거리를 현재위치 + 1로 설정
                befores[nxt] = now   # 다음 위치의 이전 위치를 현재로 저장


N, K = map(int, input().split())
dist = [0] * 100001
befores = [0] * 100001
bfs()


# 시간 초과
# from collections import deque
#
# N, K = map(int, input().split())
# q = deque([N])
# is_visit = [0] * 100001
# dists = [0] * 100001
# is_visit[N] = 0
#
# while True:
#     now = q.popleft()
#     if now == K:
#         break
#
#     for nxt in [now-1, now+1, now*2]:
#         if 0 <= nxt < 100001 and not is_visit[nxt]:
#             q.append(nxt)
#             is_visit[nxt] = now
#             dists[nxt] = dists[now] + 1
#
# answers = [K]
# while True:
#     K = is_visit[K]
#     answers.append(K)
#
#     if K == N:
#         break
#
# answers.reverse()
# print(dists[now])
# print(" ".join(map(str, answers)))


# from collections import deque
#
# N, K = map(int, input().split())
# dist = [0]*100001
# move = [0]*100001
# q = deque()
# q.append(N)
# while q:
#     x = q.popleft()
#     if x == K:
#         arr = []
#         temp = x
#         for _ in range(dist[x] + 1):
#             arr.append(temp)
#             temp = move[temp]
#         print(dist[x])
#         print(' '.join(map(str, arr[::-1])))
#         break
#     for i in (x + 1, x - 1, 2 * x):
#         if 0 <= i <= 100000 and dist[i] == 0:
#             q.append(i)
#             dist[i] = dist[x] + 1
#             move[i] = x


# 시간 초과
# from collections import deque
#
# N, K = map(int, input().split())
# q = deque([[N]])
# is_visit = {i: False for i in range(100001)}
# is_visit[N] = True
#
# while True:
#     nums = q.popleft()
#     now = nums[-1]
#     if now == K:
#         print(len(nums)-1)
#         print(*nums)
#         break
#
#     if 0 <= now-1 and not is_visit[now-1]:
#         q.append(nums + [now-1])
#         is_visit[now-1] = True
#
#     if now + 1 < 100001 and not is_visit[now+1]:
#         q.append(nums + [now+1])
#         is_visit[now+1] = True
#
#     if now * 2 < 100001 and not is_visit[now*2]:
#         q.append(nums + [now*2])
#         is_visit[now*2] = True
