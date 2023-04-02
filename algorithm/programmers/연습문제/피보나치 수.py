def solution(n):
    array = [0, 1]

    for i in range(2, n + 1):
        array.append(array[i - 1] + array[i - 2])

    return array[-1] % 1234567


print(solution(5))

# def solution(n):
#     def fibo(i):
#         if i < 2:
#             return i
#         return fibo(i-1) + fibo(i-2)
#
#     return fibo(n) %
#
