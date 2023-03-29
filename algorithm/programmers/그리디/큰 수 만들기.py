def solution(number, k):
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("654321", 1))
print(solution("654321", 5))


# from collections import deque
#
#
# def solution(number, k):
#     answer = ''
#     num = deque()
#     front = deque()
#     for n in number:
#         num.append(n)
#     while k > 0:
#         now = num.popleft()
#         if not num:
#             num = front
#             front = deque()
#             k -= 1
#             continue
#         if now == 9:
#             front.append(now)
#         elif now < num[0]:
#             for _ in range(len(front)):
#                 num.appendleft(front.pop())
#             k -= 1
#         else:
#             front.append(now)
#     for a in (front+num):
#         answer += (str(a))
#     return answer