import sys

input = sys.stdin.readline
N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]


# 행렬곱을 계산할 함수
def cross(X, Y):
    results = [[0] * N for _ in range(N)]   # 계산 결과를 담을 리스트
    for r in range(N):
        for c in range(N):
            total = 0   # 해당 칸의 값
            for i in range(N):
                total += X[r][i] * Y[i][c]
            results[r][c] = total % 1000   # 계산한 값을 1000으로 나눈 나머지를 해당 자리에 넣는다
    return results   # 결과를 반환해준다


# 제곱을 계산할 함수
def calc(mat, power):
    if power == 1:   # 제곱이 1이면
        for r in range(N):
            for c in range(N):
                mat[r][c] %= 1000   # 해당 칸의 값을 1000으로 나눈 나머지로 바꾸고
        return mat   # 반환한다
    # 제곱이 2 이상인 경우
    tmp = calc(mat, power // 2)   # 임시 행렬로 제곱을 반으로 나눈 몫만큼 제곱수로 쪼갠다
    if power % 2:   # 홀수인 경우
        return cross(cross(tmp, tmp), mat)   # 임시 행렬간의 곱과 기본 행렬의 곱을 반환한다
    else:   # 짝수인 경우
        return cross(tmp, tmp)   # 임시값끼리의 곱을 반환한다


answer = calc(matrix, B)
for ans in answer:
    print(*ans)


# 시간 초과
# import sys
# import copy
#
# input = sys.stdin.readline
# N, B = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(N)]
# answer = copy.deepcopy(matrix)
# for _ in range(B-1):
#     tmp = copy.deepcopy(answer)
#     for r in range(N):
#         for c in range(N):
#             total = 0
#             for i in range(N):
#                 total += matrix[r][i] * tmp[i][c]
#             answer[r][c] = total % 1000
#
#
# for ans in answer:
#     print(*ans)


# 시간 초과
# import copy
#
# N, B = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(N)]
# answer = copy.deepcopy(matrix)
# for _ in range(B-1):
#     tmp = copy.deepcopy(answer)
#     for r in range(N):
#         for c in range(N):
#             total = 0
#             for i in range(N):
#                 total += matrix[r][i] * tmp[i][c]
#             answer[r][c] = total
#
#
# def calc(n):
#     return n % 1000
#
#
# for ans in answer:
#     print(*map(calc, ans))
