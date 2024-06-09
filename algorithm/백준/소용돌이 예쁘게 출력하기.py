r1, c1, r2, c2 = map(int, input().split())
answers = [[0 for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]
total = (c2 - c1 + 1) * (r2 - r1 + 1)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
d = 1
r = 0
c = 0
cnt = 1
l = 1
for answer in answers:
    print(*answer)


# 시간 초과
# r1, c1, r2, c2 = map(int, input().split())
# answers = [[0 for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]
# total = (c2 - c1 + 1) * (r2 - r1 + 1)
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]
# d = 1
# r = 0
# c = 0
# cnt = 1
# l = 1
# while total:
#     for _ in range(2):
#         for _ in range(l):
#             if r1 <= r <= r2 and c1 <= c <= c2:
#                 answers[r-r1][c-c1] = cnt
#                 total -= 1
#                 m = cnt
#             r += dr[d]
#             c += dc[d]
#             cnt += 1
#         d = (d-1) % 4
#     l += 1
#
#
# for answer in answers:
#     print(*answer)
