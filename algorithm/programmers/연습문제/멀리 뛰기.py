def solution(n):
    answer = 0
    to = n // 2 + 1
    factos = [1]
    facto = 1
    for i in range(1, n+1):
        facto *= i
        factos.append(facto)
    for i in range(0, to):
        answer += factos[n-i] // (factos[n-2*i] * factos[i])
    return answer % 1234567


print(solution(4))
print(solution(6))
print(solution(5))
print(solution(3))


# def solution(num):
#     a, b = 1, 1
#     for i in range(1, num):
#         a, b = b, a+b
#     return b


# from itertools import combinations
#
#
# def solution(n):
#     answer = 0
#     to = n // 2
#     for i in range(to + 1):
#         a = 0
#         for _ in combinations(range(n - i), i):
#             a += 1
#         print(a)
#     return answer % 1234567
