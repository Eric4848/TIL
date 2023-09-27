N = int(input())
nums = list(map(int, input().split()))
answers = [-1] * N   # 정답을 초기화
stack = []   # 숫자들의 인덱스를 저장할 스택을 만든다
for i in range(N):   # 숫자들을 돌아가며
    while stack and nums[stack[-1]] < nums[i]:   # 스택이 있고, 스택의 맨 마지막이 현재 숫자보다 작을 떄
        answers[stack.pop()] = nums[i]   # 마지막 스택의 인덱스를 pop하여 그 위치에 현재 숫자를 저장한다
    stack.append(i)   # 스택의 인덱스를 저장한다
print(*answers)


# 시간 초과
# N = int(input())
# nums = list(map(int, input().split()))
# answers = [-1] * N
# ends = [nums[-1]]
# for i in range(N-2, -1, -1):
#     if nums[i] < nums[i+1]:
#         ends.append(nums[i+1])
#     for j in range(len(ends)-1, -1, -1):
#         if nums[i] < ends[j]:
#             answers[i] = ends[j]
#             break
#
# print(*answers)


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
