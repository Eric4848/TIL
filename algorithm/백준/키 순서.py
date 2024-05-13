# Pypy 제출
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
comp = [[1] * (N+1) for _ in range(N+1)]   # 비교한 내역을 1로 초기화(최소 계산으로 0을 구분할 것이므로 1)
answer = 0

# 자기 자신 변경
for i in range(1, N+1):
    comp[i][i] = 0

# 비교한 경우 변경
for _ in range(M):
    a, b = map(int, input().split())
    comp[a][b] = 0

# 플로이드 - 워셜
for k in range(1, N+1):   # 무작위 중간 지점
    for i in range(1, N+1):   # 시작 지점
        for j in range(1, N+1):   # 도착 지점
            comp[i][j] = min(comp[i][j], comp[i][k] + comp[k][j])   # 즉시 이동, 중간 걸쳐 이동 중 더 적은 것 선택

# 비교 여부 확인
for i in range(1, N+1):   # 각 학생별로
    chk = True   # 알수 있음으로 초기화
    for j in range(1, N+1):   # 모든 학생들 대상으로
        if comp[i][j] and comp[j][i]:   # 나와 대상, 대상과 나 둘 다 크고 작음을 알 수 없다면
            chk = False   # 알 수 없음으로 변경
            break   # 종료
    if chk:   # 알 수 있다면
        answer += 1   # 정답 + 1

print(answer)


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# taller = [[] for _ in range(N+1)]
# cnts = [[False] * (N+1) for _ in range(N+1)]
# answer = 0
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     taller[a].append(b)
#
# for i in range(1, N+1):
#     q = taller[i][:]
#     while q:
#         now = q.pop()
#         cnts[i][now] = True
#         cnts[now][i] = True
#         for nxt in taller[now]:
#             q.append(nxt)
#
# for cnt in cnts:
#     if sum(cnt) == N-1:
#         answer += 1
#
# print(answer)


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# taller = [[] for _ in range(N+1)]
# smaller = [[] for _ in range(N+1)]
# answer = 0
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     taller[b].append(a)
#     smaller[a].append(b)
#
# for i in range(1, N+1):
#     is_chk = [False] * (N + 1)
#     tall = taller[i][:]
#     while tall:
#         now = tall.pop()
#         is_chk[now] = True
#         for nxt in taller[now]:
#             tall.append(nxt)
#     small = smaller[i][:]
#     while small:
#         now = small.pop()
#         is_chk[now] = True
#         for nxt in smaller[now]:
#             small.append(nxt)
#
#     if sum(is_chk) == N-1:
#         answer += 1
#
# print(answer)
