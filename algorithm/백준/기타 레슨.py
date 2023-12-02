N, M = map(int, input().split())
times = list(map(int, input().split()))
minimum = max(times)
maximum = sum(times)
while minimum <= maximum:
    mid = (minimum + maximum) // 2
    total = 0
    video = 1
    for time in times:
        if mid < total + time:
            total = 0
            video += 1
        total += time

    if video <= M:
        answer = mid
        maximum = mid - 1
    else:
        minimum = mid + 1
print(answer)


# 오답
# N, M = map(int, input().split())
# nums = list(map(int, input().split()))
# avg = sum(nums) / M
# tmp = 0
# answers = []
# for i in range(len(nums)):
#     # if tmp < avg:
#     #     tmp += nums[i]
#     # else:
#     #     answers.append(tmp)
#     #     tmp = nums[i]
#     if avg < tmp + nums[i]:
#         answers.append(tmp + nums[i])
#         tmp = nums[i]
#     else:
#         tmp += nums[i]
#
# print(min(answers))
