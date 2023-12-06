import heapq

heap = []   # 힙 초기화
N = int(input())

for _ in range(N):
    nums = map(int, input().split())
    for num in nums:   # 각 줄별로
        if len(heap) < N:   # 힙 크기가 N보다 작다면
            heapq.heappush(heap, num)   # 힙에 추가한다
        else:   # 힙 크기가 N개 이상이면
            if heap[0] < num:   # 힙의 가장 작은 수보다 현재 숫자가 크면
                heapq.heappop(heap)   # 가장 작은 수를 제거하고
                heapq.heappush(heap, num)   # 현재 숫자를 힙에 추가한다
print(heap[0])


# 메모리 초과
# import sys
#
# input = sys.stdin.readline
# N = int(input())
# over_nums = []
# for i in range(N):
#     nums = list(map(int, input().split()))
#     nums += over_nums
#     nums.sort()
#     over_nums = nums[N-1-i:]
# print(nums[-N])


# 메모리 초과
# N = int(input())
# nums = [[] for _ in range(N)]
# for _ in range(N):
#     inputs = list(map(int, input().split()))
#     for i in range(N):
#         nums[i].append(inputs[i])
#
# for _ in range(N):
#     maximum = float('-inf')
#     for i in range(N):
#         if maximum < nums[i][-1]:
#             maximum = nums[i][-1]
#             location = i
#     nums[location].pop()
# print(maximum)


# 메모리 초과
# N = int(input())
# nums = [list(map(int, input().split())) for _ in range(N)]
# delta = [1] * N
# location = 0
# for _ in range(N):
#     maximum = float('-inf')
#     for i in range(N):
#         if maximum < nums[N-delta[i]][i]:
#             maximum = nums[N-delta[i]][i]
#             location = i
#     delta[location] += 1
# print(maximum)
