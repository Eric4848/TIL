import heapq


def solution(operations):
    answer = []
    store = []
    temp = []
    heapq.heapify(temp)
    heapq.heapify(store)
    for operation in operations:
        do, operate = operation.split()
        operate = int(operate)
        if do == 'I':
            heapq.heappush(store, operate)
        elif do == 'D':
            if store:
                if operate == 1:
                    for _ in range(1, len(store)):
                        heapq.heappush(temp, heapq.heappop(store))
                    heapq.heappop(store)
                    for _ in range(len(temp)):
                        heapq.heappush(store, heapq.heappop(temp))
                elif operate == -1:
                    heapq.heappop(store)
    if store:
        answer.append(max(store))
        answer.append(min(store))
    else:
        answer = [0, 0]
    return answer


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))

# from heapq import heappush, heappop
#
# def solution(arguments):
#     max_heap = []
#     min_heap = []
#     for arg in arguments:
#         if arg == "D 1":
#             if max_heap != []:
#                 heappop(max_heap)
#                 if max_heap == [] or -max_heap[0] < min_heap[0]:
#                     min_heap = []
#                     max_heap = []
#         elif arg == "D -1":
#             if min_heap != []:
#                 heappop(min_heap)
#                 if min_heap == [] or -max_heap[0] < min_heap[0]:
#                     max_heap = []
#                     min_heap = []
#         else:
#             num = int(arg[2:])
#             heappush(max_heap, -num)
#             heappush(min_heap, num)
#     if min_heap == []:
#         return [0, 0]
#     return [-heappop(max_heap), heappop(min_heap)]
