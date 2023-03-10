def solution(n, works):
    answer = 0
    total = sum(works)
    hour = len(works)
    if total > n:
        works.sort()
        num = 0
        for _ in range(n):
            works[-1 - num] -= 1
            if num == hour-1:
                num = 0

            elif works[-1 - num] == works[-2 - num]:
                num = 0

            elif works[-1 - num] < works[-2 - num]:
                num += 1

            elif works[-2 - num] < works[-1 - num]:
                num = 0

        answer = sum(h ** 2 for h in works)
    return answer


print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))
print(solution(999, [800, 100, 55, 45]))
print(solution(9, [1, 1, 1]))
print(solution(99, [2, 15, 22, 55, 55]))

# from heapq import heapify, heappush, heappop
# def solution(n, works):
#     heapify(works := [-i for i in works])
#     for i in range(min(n, abs(sum(works)))):
#         heappush(works, heappop(works)+1)
#     return sum([i*i for i in works])
