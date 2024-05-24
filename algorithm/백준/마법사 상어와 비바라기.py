import sys

input = sys.stdin.readline
N, M = map(int, input().split())
# 이동 방향 설정(0번째는 인덱스를 위해 0)
dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]
baskets = [list(map(int, input().split())) for _ in range(N)]
clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]   # 시작 구름 위치
for _ in range(M):   # 이동 마다
    is_visit = [[False] * N for _ in range(N)]   # 구름이 도착한 위치 정보 초기화
    rains = []   # 비가 내릴 곳을 저장할 리스트
    d, s = map(int, input().split())   # 이동 방향, 거리
    while clouds:   # 구름 좌표 만큼
        # 좌표를 명령대로 이동
        r, c = clouds.pop()
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N
        # 도착지지에 비를 내리고 비내린 위치 저장, 방문 처리
        baskets[nr][nc] += 1
        rains.append([nr, nc])
        is_visit[nr][nc] = True

    # 물복사 마법
    for r, c in rains:   # 비내린 위치마다
        for i in range(2, 9, 2):   # 대각 방향별로
            nr = r + dr[i]
            nc = c + dc[i]
            # 조건에 맞으면 + 1
            if 0 <= nr < N and 0 <= nc < N and baskets[nr][nc]:
                baskets[r][c] += 1

    # 구름 생성
    for r in range(N):
        for c in range(N):
            if 1 < baskets[r][c] and not is_visit[r][c]:   # 구름 생성이 가능하고, 구름이 방문한 곳이 아니라면
                baskets[r][c] -= 2   # 물을 2만큼 줄이고
                clouds.append([r, c])   # 구름에 추가

# 정답 계산
answer = 0
for b in baskets:
    answer += sum(b)
print(answer)


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
# dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]
# baskets = [list(map(int, input().split())) for _ in range(N)]
# clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
# rains = []
# for _ in range(M):
#     d, s = map(int, input().split())
#     while clouds:
#         r, c = clouds.pop()
#         nr = (r + dr[d] * s) % N
#         nc = (c + dc[d] * s) % N
#         baskets[nr][nc] += 1
#         rains.append([nr, nc])
#
#     for r, c in rains:
#         for i in range(2, 9, 2):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nr < N and 0 <= nc < N and baskets[nr][nc]:
#                 baskets[r][c] += 1
#
#     for r in range(N):
#         for c in range(N):
#             if [r, c] in rains:
#                 rains.remove([r, c])
#             elif 1 < baskets[r][c]:
#                 baskets[r][c] -= 2
#                 clouds.append([r, c])
#
# answer = 0
# for b in baskets:
#     answer += sum(b)
# print(answer)
