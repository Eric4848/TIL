# 시간 초과
N = int(input())
nums = list(map(int, input().split()))
nums.sort()
answer = 0
for i in range(2, N):
    chk = 0
    for a in range(0, i-1):
        if chk:
            break
        for b in range(i-1, a, -1):
            if nums[a] + nums[b] == nums[i]:
                answer += 1
                chk = 1
                break

print(answer)


# 시간 초과
# N = int(input())
# nums = list(map(int, input().split()))
# answer = 0
# for i in range(2, N):
#     chk = 0
#     for j in range(0, i):
#         if chk:
#             break
#         for k in range(j, i):
#             if j != k:
#                 if nums[j] + nums[k] == nums[i]:
#                     answer += 1
#                     chk = 1
#                     break
# print(answer)
