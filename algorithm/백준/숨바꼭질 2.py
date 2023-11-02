from collections import deque

N, K = map(int, input().split())
q = deque([N])
counts = [0] * 100001   # 도달까지 걸린 횟수를 0으로 초기화
answer = 0   # 최소로 도착할 수 있는 경우의 수를 0으로 초기화

while q:
    now = q.popleft()   # 현재 위치
    if now == K:   # 현재 위치가 목적지라면
        answer += 1   # 최소 경우의 수를 1 추가하고
        continue   # 다음 큐의 원소로 넘긴다

    for nxt in [now+1, now-1, now*2]:   # 앞,뒤 한칸과 2배 이동의 경우들중
        if 0 <= nxt <= 100000 and (counts[nxt] == 0 or counts[nxt] == counts[now] + 1):   # 제한 범위 이내고, 도착한 적 없거나 도착까지 걸린 횟수가 이전과 같다면
            counts[nxt] = counts[now] + 1   # 도착까지 걸린 횟수를 현재위치까지 걸린횟수 + 1로 변경하고(0조건으로 최소 횟수로 저장된다)
            q.append(nxt)   # 해당 도착지를 큐에 추가한다

print(counts[K])   # 도착지까지 필요한 최소 횟수와
print(answer)   # 가능한 경우의수를 출력


# 시간 초과
# from collections import deque
#
# N, K = map(int, input().split())
# q = deque([[N, 0]])
# answer = 100001
# answer_cnt = 0
# while q:
#     now, count = q.popleft()
#     if answer < count:
#         break
#
#     if now == K:
#         answer = count
#         answer_cnt += 1
#         continue
#
#     if 0 < now:
#         q.append([now-1, count+1])
#
#     if now < 100001:
#         q.append([now+1, count+1])
#
#     if now <= 50000:
#         q.append([now*2, count+1])
#
# print(answer)
# print(answer_cnt)
