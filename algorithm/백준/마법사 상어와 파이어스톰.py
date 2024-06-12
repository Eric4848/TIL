# Pypy3 제출
import sys
from collections import deque


# 회전시키는 함수
def rot(rank):
    d = 2 ** rank   # 회전시키는 단위 칸 수
    for i in range(0, l, d):   # 행 시점
        for j in range(0, l, d):   # 열 시점
            for r in range(d):   # 행 길이
                for c in range(d):   # 열 길이
                    tmps[c + i][d - r - 1 + j] = ices[r + i][c + j]   # 원본의 위치 값을 돌린 위치에 저장


input = sys.stdin.readline
N, Q = map(int, input().split())
l = 2 ** N   # 총 길이
ices = [list(map(int, input().split())) for _ in range(l)]
tmps = [[0] * l for _ in range(l)]   # 회전 시 저장할 리스트
ranks = list(map(int, input().split()))
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
# 마법 시전
for rank in ranks:   # 단계별로
    rot(rank)   # 회전
    # 회전 값 저장
    for r in range(l):
        for c in range(l):
            ices[r][c] = tmps[r][c]
    # 회전 후 줄어드는 값 계산
    for r in range(l):
        for c in range(l):
            cnt = 0   # 인접 얼음 갯수 초기화
            for i in range(4):   # 방향별로
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < l and 0 <= nc < l and tmps[nr][nc]:   # 범위 내, 해당칸이 얼음이라면(임시칸 기준)
                    cnt += 1   # 갯수 + 1
            if cnt < 3 and ices[r][c]:   # 인접 얼음 갯수가 3보다 작고, 원본에 얼음이 있다면
                ices[r][c] -= 1   # 1 감소
# 정답 계산
is_visit = [[False] * l for _ in range(l)]   # 방문 초기화
total = 0   # 총 얼음 갯수 초기화
size = 0   # 최대 크기 초기화
for r in range(l):
    for c in range(l):
        if ices[r][c]:   # 얼음이 있다면
            total += ices[r][c]   # 총량에 추가
            if not is_visit[r][c]:   # 방문한 적 없는 곳이라면
                q = deque([(r, c)])   # deque에 해당 위치 추가
                tmp = 1   # 덩어리 크기 1
                is_visit[r][c] = True   # 방문 처리
                while q:   # bfs진행
                    R, C = q.popleft()
                    for i in range(4):   # 방향별로
                        nr = R + dr[i]
                        nc = C + dc[i]
                        # 범위 내, 방문한 적 없고 얼음이 있다면
                        if 0 <= nr < l and 0 <= nc < l and not is_visit[nr][nc] and ices[nr][nc]:
                            tmp += 1   # 크기 + 1
                            q.append((nr, nc))   # 해당 위치 큐에 추가
                            is_visit[nr][nc] = True   # 방문 처리
                size = max(size, tmp)   # 최대 크기와 비교하여 큰 것 저장
print(total)
print(size)


# 시간 초과
# import sys
# from collections import deque
#
#
# def rot(rank):
#     d = 2 ** rank
#     for i in range(0, l, d):
#         for j in range(0, l, d):
#             for r in range(d):
#                 for c in range(d):
#                     tmps[c + i][d - r - 1 + j] = ices[r + i][c + j]
#
#
# input = sys.stdin.readline
# N, Q = map(int, input().split())
# l = 2 ** N
# ices = [list(map(int, input().split())) for _ in range(l)]
# tmps = [[0] * l for _ in range(l)]
# ranks = list(map(int, input().split()))
# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]
# for rank in ranks:
#     rot(rank)
#     for r in range(l):
#         for c in range(l):
#             ices[r][c] = tmps[r][c]
#     for r in range(l):
#         for c in range(l):
#             cnt = 0
#             for i in range(4):
#                 nr = r + dr[i]
#                 nc = c + dc[i]
#                 if 0 <= nr < l and 0 <= nc < l and tmps[nr][nc]:
#                     cnt += 1
#             if cnt < 3 and ices[r][c]:
#                 ices[r][c] -= 1
#
# is_visit = [[False] * l for _ in range(l)]
# total = 0
# size = 0
# for r in range(l):
#     for c in range(l):
#         if ices[r][c]:
#             total += ices[r][c]
#             if not is_visit[r][c]:
#                 q = deque([(r, c)])
#                 tmp = 1
#                 is_visit[r][c] = True
#                 while q:
#                     R, C = q.popleft()
#                     for i in range(4):
#                         nr = R + dr[i]
#                         nc = C + dc[i]
#                         if 0 <= nr < l and 0 <= nc < l and not is_visit[nr][nc] and ices[nr][nc]:
#                             tmp += 1
#                             q.append((nr, nc))
#                             is_visit[nr][nc] = True
#                 size = max(size, tmp)
# print(total)
# print(size)
