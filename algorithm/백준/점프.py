N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = [[0] * N for _ in range(N)]   # 정답을 N X N의 배열에 0을 넣어주고
answer[0][0] = 1   # 처음 위치를 1로 바꾸어준다(이동 가능 회수)

for r in range(N):   # 열과
    for c in range(N):   # 행을 돌아가며
        if r == c == N - 1:   # 마지막 칸인 경우
            print(answer[-1][-1])   # 이동 가능 횟수를 출력한다
            break

        jump = matrix[r][c]   # 해당 위치에서 이동해야하는 거리를 불러와서

        if r + jump < N:   # 아래로 이동했을 때 범위 이내이면
            answer[r + jump][c] += answer[r][c]   # 이동한 위치까지 이동 가능 횟수에 출발 위치까지 이동 가능 횟수를 더해준다
        if c + jump < N:
            answer[r][c + jump] += answer[r][c]


# 최소 횟수로 착각하여 푼 정답
# from collections import deque
#
# N = int(input())
# matrix = [list(map(int, input().split())) for _ in range(N)]
# answer = [[float('inf')] * N for _ in range(N)]
# answer[0][0] = 0
# q = deque()
# q.append((0, 0))
#
# while q:
#     r, c = q.popleft()
#     jump = matrix[r][c]
#     nr = r + jump
#     nc = c + jump
#     cnt = answer[r][c] + 1
#
#     if nr < N:
#         if cnt < answer[nr][c]:
#             answer[nr][c] = cnt
#             q.append((nr, c))
#
#     if nc < N:
#         if cnt < answer[r][nc]:
#             answer[r][nc] = cnt
#             q.append((r, nc))
#
#     if r == c == N-1:
#         print(answer)

# 시간초과
# import sys
# input = sys.stdin.readline
# N = int(input())
# matrix = [list(map(int, input().split())) for _ in range(N)]
# q = [(0, 0)]
# answer = [0]
#
#
# def dfs(r, c):
#     if r == c == N - 1:
#         answer[0] += 1
#         return
#     jump = matrix[r][c]
#     nr = r + jump
#     nc = c + jump
#
#     if nr < N:
#         dfs(nr, c)
#
#     if nc < N:
#         dfs(r, nc)
#
#
# dfs(0, 0)
# print(answer[0])
