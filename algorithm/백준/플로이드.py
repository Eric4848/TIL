# 플로이드 워셜
n = int(input())
m = int(input())
bus = [[float('inf')] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    bus[a][b] = min(bus[a][b], c)

for k in range(1, n+1):   # 경유지
    for i in range(1, n+1):   # 출발지
        for j in range(1, n+1):   # 도착지
            if i == j:   # 출발지와 도착지가 같으면
                bus[i][j] = 0   # 이동시간을 0으로 설정
            else:   # 아닌 경우
                bus[i][j] = min(bus[i][j], bus[i][k] + bus[k][j])   # 경유지를 거치는 것과 바로 가는 것중 더 적은 시간을 선택

for s in range(1, n+1):
    for e in range(1, n+1):
        if bus[s][e] == float('inf'):   # 도착할 수 없으면
            print('0', end=' ')   # 0 출력
        else:   # 아닌 경우
            print(bus[s][e], end=' ')   # 저장된 시간 출력
    print()   # 줄바꿈


# 시간 초과
# from collections import deque
#
# n = int(input())
# m = int(input())
# bus = [[] for _ in range(n+1)]
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     bus[a].append((b, c))
# answers = [[float('inf')] * (n+1) for _ in range(n+1)]
#
# for starts in range(1, n+1):
#     answers[starts][starts] = 0
#     q = deque()
#     q.append(starts)
#     while q:
#         s = q.popleft()
#         for e, l in bus[s]:
#             if answers[starts][s] + l < answers[starts][e]:
#                 q.append(e)
#                 answers[starts][e] = answers[starts][s] + l
#
# for i in range(1, n+1):
#     print(*answers[i][1:])
