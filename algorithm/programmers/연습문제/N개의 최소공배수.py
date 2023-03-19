import math


def lcm(a, b):   # 최소 공배수를 구하는 함수
    return int(a * b / math.gcd(a, b))   # 두 수의 곱을 최대 공약수로 나누면 최소 공배수가된다


def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):   # 모든 숫자의 최소 공배수를 반복하여 구한다
        answer = lcm(answer, arr[i])
    return answer


print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))
print(solution([17, 34]))
print(solution([12, 32, 45, 67, 72]))
print(solution([3, 4, 9, 16]))
