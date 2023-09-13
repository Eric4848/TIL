# 실패(갯수 세어 계산)
N, M, B = map(int, input().split())
grounds = [list(map(int, input().split())) for _ in range(N)]
answer = 0
cnts = {}
for i in range(N):
    for j in range(M):
        height = grounds[i][j]
        if height in cnts:
            cnts[height] += 1
        else:
            cnts[height] = 1
maximum = max(cnts.values())
for k in cnts.keys():
    if cnts[k] == maximum:
        idx = k

while True:
    add = 0
    sub = 0
    for i in cnts.keys():
        if idx < i:
            sub += 1
        elif i < idx:
            add += 1

    if add <= B + sub:
        answer = add + 2 * sub
        break
    else:
        idx -= 1
        answer = 0
print(answer, idx)


# 시간초과
# import sys
#
# input = sys.stdin.readline
# N, M, B = map(int, input().split())
# grounds = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# answer = float('inf')
# height = 0
# for i in range(max(map(max, grounds)), min(map(min, grounds)) - 1, -1):
#     add = 0
#     sub = 0
#     for r in range(N):
#         for c in range(M):
#             if grounds[r][c] < i:
#                 add += i - grounds[r][c]
#             else:
#                 sub += grounds[r][c] - i
#     if add < sub + B:
#         times = add + 2 * sub
#         if times < answer:
#             answer = times
#             height = i
#
# print(answer, height)