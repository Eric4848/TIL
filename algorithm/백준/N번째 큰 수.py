# 메모리 초과
import sys

input = sys.stdin.readline
N = int(input())
over_nums = []
for i in range(N):
    nums = list(map(int, input().split()))
    nums += over_nums
    nums.sort()
    over_nums = nums[N-1-i:]
print(nums[-N])


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
