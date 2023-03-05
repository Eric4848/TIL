def solution(triangle):
    sums = [[] for _ in range(len(triangle))]
    sums[0].append(triangle[0][0])
    for n in range(1, len(triangle)):
        for i in range(len(triangle[n])):
            if i == 0:
                sums[n].append(sums[n-1][0]+triangle[n][0])
            elif i == len(triangle[n])-1:
                sums[n].append(sums[n-1][i-1]+triangle[n][i])
            else:
                if sums[n-1][i-1] > sums[n-1][i]:
                    sums[n].append(sums[n-1][i-1]+triangle[n][i])
                else:
                    sums[n].append(sums[n-1][i]+triangle[n][i])
    return max(sums[len(triangle)-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))


# def solution(triangle):
#     dp = []
#     for t in range(1, len(triangle)):
#         for i in range(t+1):
#             if i == 0:
#                 triangle[t][0] += triangle[t-1][0]
#             elif i == t:
#                 triangle[t][-1] += triangle[t-1][-1]
#             else:
#                 triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
#     return max(triangle[-1])


# def solution(triangle):
#     answer = 0
#
#     def search(idx, total, loc):
#         nonlocal answer
#         if idx == len(triangle):
#             if answer < total:
#                 answer = total
#             return
#
#         for i in range(loc, loc+2):
#             search(idx+1, total+triangle[idx][i], i)
#
#     search(1, triangle[0][0], 0)
#
#     return answer
