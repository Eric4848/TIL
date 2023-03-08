from collections import deque


def solution(maps):
    to_visit = deque()
    to_visit.append((0, 0))
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    while to_visit:
        r, c = to_visit.popleft()
        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]
            if 0 <= new_r < len(maps) and 0 <= new_c < len(maps[0]) and maps[new_r][new_c] == 1:
                maps[new_r][new_c] += maps[r][c]
                to_visit.append((new_r, new_c))
    answer = maps[len(maps)-1][len(maps[0])-1]
    if answer == 1:
        answer -= 2
    return answer


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))

# def solution(maps):
#     answer = float('INF')
#
#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]
#
#     def next_step(r, c, move):
#         nonlocal answer
#         maps[r][c] = 0
#         if r + 1 == len(maps) and c + 1 == len(maps[0]):
#             if move < answer:
#                 answer = move
#             return
#
#         for i in range(4):
#             if answer < move:
#                 break
#             if r + dr[i] == len(maps) or c + dc[i] == len(maps[0]) or r + dr[i] == -1 or c + dc[i] == -1:
#                 continue
#             if maps[r + dr[i]][c + dc[i]] == 1:
#                 next_step(r + dr[i], c + dc[i], move + 1)
#                 maps[r + dr[i]][c + dc[i]] = 1
#
#         return
