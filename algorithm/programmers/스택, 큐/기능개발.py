import math


def solution(progresses, speeds):
    answer = []
    works = []
    temp = 1
    for i in range(len(progresses)):
        work = math.ceil((100 - progresses[i]) / speeds[i])

        if i == 0:
            works.append(work)

        else:
            if works[i-1] > work:
                works.append(works[i-1])
                temp += 1
            else:
                works.append(work)
                answer.append(temp)
                temp = 1

            if i == len(progresses) - 1:
                answer.append(temp)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))


# def solution(progresses, speeds):
#     print(progresses)
#     print(speeds)
#     answer = []
#     time = 0
#     count = 0
#     while len(progresses) > 0:
#         if (progresses[0] + time*speeds[0]) >= 100:
#             progresses.pop(0)
#             speeds.pop(0)
#             count += 1
#         else:
#             if count > 0:
#                 answer.append(count)
#                 count = 0
#             time += 1
#     answer.append(count)
#     return answer