def solution(n):
    answer = ''
    while n > 0:
        left = n % 3
        n //= 3
        if left == 0:
            answer = '4' + answer
            n -= 1
        else:
            answer = str(left) + answer
    return answer


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))


# def change124(n):
#     num = ['1', '2', '4']
#     answer = ""
#
#     while n > 0:
#         n -= 1
#         answer = num[n % 3] + answer
#         n //= 3
#
#     return answer
#
#
# print(change124(10))
