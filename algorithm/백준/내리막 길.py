import sys

input = sys.stdin.readline
N, M = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]   # 지나갈 수 있는지 저장하는 dp를 -1로 초기화한다
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


# 다음으로 갈 수 있으면 다음에서 도착할 수 있는 경우의 수들을 저장
def search(r, c):
    # 도착지점에 도달한 경우
    if r == N-1 and c == M-1:
        return 1   # 갈 수 있는 방법 1개

    # 이미 지나가 본 길인 경우
    if dp[r][c] != -1:
        return dp[r][c]   # 현재 갈 수 있는 길 만큼

    dp[r][c] = 0   # 갈 방법이 없다고 처리

    for i in range(4):   # 4방향으로
        nr = r + dr[i]
        nc = c + dc[i]
        # 범위 이내이며 이전 위치보다 낮다면
        if 0 <= nr < N and 0 <= nc < M and heights[nr][nc] < heights[r][c]:
            dp[r][c] += search(nr, nc)   # 다음 방향의 갯수를 현재 가짓수에 더해준다

    return dp[r][c]   # 현재 갈 수 있는 길 만큼 반환


print(search(0, 0))


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# heights = [list(map(int, input().split())) for _ in range(N)]
# answer = [0]
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
#
#
# def search(r, c, now):
#     if r == N-1 and c == M-1:
#         answer[0] += 1
#         return
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < N and 0 <= nc < M and heights[nr][nc] < now:
#             search(nr, nc, heights[nr][nc])
#
#
# search(0, 0, heights[0][0])
# print(answer[0])


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# heights = [list(map(int, input().split())) for _ in range(N)]
# is_visit = [[False] * M for _ in range(N)]
# answer = [0]
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
#
#
# def search(r, c):
#     if r == N-1 and c == M-1:
#         answer[0] += 1
#         return
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < N and 0 <= nc < M and not is_visit[nr][nc] and heights[nr][nc] < heights[r][c]:
#             is_visit[nr][nc] = True
#             search(nr, nc)
#             is_visit[nr][nc] = False
#
#
# search(0, 0)
# print(answer[0])
