from collections import deque


def solution(priorities, location):
    answer = 1
    priorities = deque(priorities)
    my_docs = [0 for _ in priorities]
    my_docs[location] = 1
    check = 0
    maximum = max(priorities)
    while 1:
        if priorities[0] == maximum:
            if my_docs[check] == 1:
                break
            priorities.popleft()
            answer += 1
            priorities.append(-1)
            maximum = max(priorities)
        else:
            priorities.append(priorities.popleft())
        check += 1
        if check == len(priorities):
            check = 0

    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))


# def solution(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]
#     answer = 0
#     while True:
#         cur = queue.pop(0)
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer
