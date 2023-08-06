# KeyboardInterrupt
# N, M = map(int, input().split())
# r, c, d = map(int, input().split())
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]
# answer = 0
# total = 0
# matrix = [list(map(int, input().split())) for _ in range(N)]
# for i in range(M):
#     total += sum(matrix[i])
#
# while total != (N * M):
#     answer += 1
#     if matrix[r][c] == 0:
#         total += 1
#         matrix[r][c] = 1
#
#     chk = 0
#     for i in range(1, 5):
#         d -= i
#         if d < 0:
#             d += 4
#         nr = r + dr[d]
#         nc = c + dc[d]
#         if 0 <= nr < N and 0 <= nc < M:
#             if matrix[nr][nc] == 0:
#                 r = nr
#                 c = nc
#                 chk = 1
#                 break
#     if not chk:
#         d -= 1
#         if d < 0:
#             d += 4
#         nr = r - dr[d]
#         nc = c - dc[d]
#         if 0 < nr < N and 0 <= nc < M:
#             r = nr
#             c = nc
#         else:
#             break
# print(answer)
