def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    j = 0

    for i in range(len(A)):
        if A[j] < B[i]:
            answer = answer + 1
            j = j + 1

    return answer


print(solution([5, 1, 3, 7], [2, 2, 6, 8]))

# from collections import deque
#
#
# def solution(A, B):
#     answer = 0
#     A.sort()
#     B.sort()
#     A = deque(A)
#     B = deque(B)
#     while A:
#         if A[-1] < B[-1]:
#             answer += 1
#             A.pop()
#             B.pop()
#         else:
#             A.pop()
#             B.popleft()
#
#     return answer

# def solution(A, B):
#     answer = 0
#     A.sort(reverse=True)
#     B.sort(reverse=True)
#     is_done = [False] * len(B)
#     for a in A:
#         check = -1
#         for b in range(len(B)):
#             if not is_done[b]:
#                 if B[b] > a:
#                     check = b
#                 if check != -1:
#                     is_done[check] = True
#                     answer += 1
#                     break
#
#     return answer
