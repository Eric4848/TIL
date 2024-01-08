n, m = map(int, input().split())
maps = [list(map(int, input().strip())) for _ in range(n)]
answer = 0
for r in range(1, n):
    for c in range(1, m):
        if maps[r][c]:
            chk = 1
            for i in range(maps[r-1][c-1]):
                if not maps[r-1-i][c] or not maps[r][c-1-i]:
                    chk = 0
                    break

            if chk:
                maps[r][c] = maps[r-1][c-1] + 1
                answer = max(answer, maps[r][c] ** 2)
print(answer)


# 오답
# n, m = map(int, input().split())
# maps = [list(map(int, input().strip())) for _ in range(n)]
# answer = 0
# for r in range(1, n):
#     for c in range(1, m):
#         if answer <= maps[r][c]:
#             chk = 1
#             for i in range(maps[r-1][c-1]):
#                 if not maps[r-1-i][c] or not maps[r][c-1-i]:
#                     chk = 0
#                     break
#
#             if chk:
#                 maps[r][c] = maps[r-1][c-1] + 1
#                 answer = max(answer, maps[r][c])
# print(answer)


# 시간 초과
# n, m = map(int, input().split())
# maps = [list(map(int, input().strip())) for _ in range(n)]
# answer = 0
# for r in range(1, n):
#     for c in range(1, m):
#         if maps[r][c]:
#             chk = 1
#             for i in range(maps[r-1][c-1]):
#                 if not maps[r-1-i][c] or not maps[r][c-1-i]:
#                     chk = 0
#                     break
#
#             if chk:
#                 maps[r][c] = maps[r-1][c-1] + 1
#                 answer = max(answer, maps[r][c])
# print(answer)
