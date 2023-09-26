# 시간 초과
N = int(input())
nums = list(map(int, input().split()))
answers = [-1] * N
ends = [nums[-1]]
for i in range(N-2, -1, -1):
    if nums[i] < nums[i+1]:
        ends.append(nums[i+1])
    for j in range(len(ends)-1, -1, -1):
        if nums[i] < ends[j]:
            answers[i] = ends[j]
            break

print(*answers)


# 오답
# N = int(input())
# nums = list(map(int, input().split()))
# answers = [-1] * N
# end = nums[-1]
# for i in range(N-2, -1, -1):
#     if nums[i] < nums[i+1]:
#         answers[i] = nums[i+1]
#         # end = max(end, nums[i+1])
#
#     elif nums[i] < end:
#         answers[i] = end
#
# print(*answers)


# 시간 초과
# N = int(input())
# nums = list(map(int, input().split()))
# for i in range(N):
#     answer = -1
#     now = nums[i]
#     for j in range(i+1, N):
#         if now < nums[j]:
#             answer = nums[j]
#             break
#     print(answer, end=' ')
