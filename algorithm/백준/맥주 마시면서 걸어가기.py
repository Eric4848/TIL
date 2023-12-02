import sys
from collections import deque

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    home = list(map(int, input().split()))   # 집 위치
    convs = [list(map(int, input().split())) for _ in range(N)]   # 편의점 위치들
    festival = list(map(int, input().split()))   # 공연장 위치
    is_visit = [False] * N   # 편의점의 방문여부
    chk = 0   # 도착할 수 없다고 초기화
    q = deque([home])   # deque에 출발지인 집 위치를 넣어준다

    while q:
        now = q.popleft()   # 현재 위치를 큐에서 popleft로 가져온다
        if abs(now[0] - festival[0]) + abs(now[1] - festival[1]) <= 1000:   # 현재 위치가 목적지와 맨해탄 거리가 1000 이하면
            chk = 1   # 갈 수 있다 처리
            break   # 반복문 종료
        for i in range(N):   # 편의점들 중
            if not is_visit[i]:   # 방문하지 않았고
                if abs(now[0] - convs[i][0]) + abs(now[1] - convs[i][1]) <= 1000:   # 현재 위치와 맨해탄 거리가 1000 이하면
                    is_visit[i] = True   # 방문처리하고
                    q.append(convs[i])   # 큐에 편의점 위치를 넣어준다

    if chk:
        print('happy')
    else:
        print('sad')


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     home = list(map(int, input().split()))
#     convs = [list(map(int, input().split())) for _ in range(N)]
#     festival = list(map(int, input().split()))
#     is_visit = [False] * N
#     chk = 0
#
#
#     def move(now):
#         global chk
#         if abs(now[0] - festival[0]) + abs(now[1] - festival[1]) <= 1000:
#             chk = 1
#             return
#         for i in range(N):
#             if not is_visit[i]:
#                 if abs(now[0] - convs[i][0]) + abs(now[1] - convs[i][1]) <= 1000:
#                     is_visit[i] = True
#                     move(convs[i])
#                     is_visit[i] = False
#     move(home)
#     if chk:
#         print('happy')
#     else:
#         print('sad')
