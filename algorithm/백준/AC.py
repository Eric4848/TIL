from collections import deque

T = int(input())
for _ in range(T):
    todos = input()
    N = int(input())
    nums = deque(input()[1:-1].split(','))
    r = 0

    if N == 0:
        nums = []

    for todo in todos:
        if todo == 'D':
            if len(nums) == 0:
                print('error')
                check = 1
                break
            else:
                if r % 2 == 0:
                    nums.popleft()
                else:
                    nums.pop()
        else:
            r += 1
    else:
        if r % 2 == 1:
            nums.reverse()
        print('[' + ','.join(nums) + ']')


# 매번 reverse 적용 시 시간 초과
# from collections import deque
#
# T = int(input())
# for _ in range(T):
#     todos = [A for A in input()]
#     N = int(input())
#
#     if N != 0:
#         nums = list(map(str, input().strip('[]').split(',')))
#     else:
#         nums = []
#
#     if todos.count('D') >= N:
#         print('error')
#     else:
#         step = 0
#         nums = deque(nums)
#         while step < len(todos):
#             if todos[step] == 'D':
#                 nums.popleft()
#                 step += 1
#             else:
#                 if step+1 < len(todos):
#                     if todos[step+1] == 'R':
#                         step += 2
#                     else:
#                         nums.reverse()
#                         step += 1
#                 else:
#                     nums.reverse()
#                     step += 1
#
#         print("[", end="")
#         print(*nums, sep=",", end="")
#         print("]")

        # print('[' + ','.join(nums)+']')

        # answer = '['
        # for num in nums:
        #     answer += str(num) + ','
        # answer = answer[:-1]
        # answer += ']'
        # print(answer)

