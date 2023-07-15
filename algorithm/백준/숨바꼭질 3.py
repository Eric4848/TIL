from collections import deque

start, end = map(int, input().split())
checks = deque()  # bfs방문할 리스트를 deque로 만든다
checks.append(start)  # 방문 리스트에 시작 위치 저장
counts = [-1] * 100001  # 위치까지 걸린 시간을 저장할 리스트
counts[start] = 0  # 시작 위치의 시간을 0으로 변경

while counts[end] == -1:  # 도착지점에 도착하기 전까지
    now = checks.popleft()
    if now * 2 < 100001 and counts[now * 2] == -1:   # 확인 여부를 거리를 바꾸었는지로 확인 가능
        checks.appendleft(now * 2)  # 걸린 시간이 0이므로 먼저 확인하기 위해 appendleft를 사용
        counts[now * 2] = counts[now]

    if now + 1 < 100001 and counts[now + 1] == -1:
        checks.append(now + 1)  # 걸린 시간이 1이므로 append를 사용하여 나중에 확인
        counts[now + 1] = counts[now] + 1

    if 0 <= now - 1 and counts[now - 1] == -1:
        checks.append(now - 1)
        counts[now - 1] = counts[now] + 1

print(counts[end])

# from collections import deque
#
# start, end = map(int, input().split())
# is_checked = [False] * 100001   # bfs를 위해 방문했는지 확인
# checks = deque()   # bfs방문할 리스트를 deque로 만든다
# checks.append(start)   # 방문 리스트에 시작 위치 저장
# is_checked[start] = True   # 시작위치 방문처리
# counts = [-1] * 100001   # 위치까지 걸린 시간을 저장할 리스트
# counts[start] = 0   # 시작 위치의 시간을 0으로 변경
#
#
# while counts[end] == -1:   # 도착지점에 도착하기 전까지
#     now = checks.popleft()
#     if now * 2 < 100001 and not is_checked[now * 2]:
#         checks.appendleft(now * 2)   # 걸린 시간이 0이므로 먼저 확인하기 위해 appendleft를 사용
#         is_checked[now * 2] = True
#         counts[now * 2] = counts[now]
#
#     if now + 1 < 100001 and not is_checked[now + 1]:
#         checks.append(now + 1)   # 걸린 시간이 1이므로 append를 사용하여 나중에 확인
#         is_checked[now + 1] = True
#         counts[now + 1] = counts[now] + 1
#
#     if 0 <= now - 1 and not is_checked[now - 1]:
#         checks.append(now - 1)
#         is_checked[now - 1] = True
#         counts[now - 1] = counts[now] + 1
#
# print(counts[end])
