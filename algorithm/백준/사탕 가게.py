# import sys
#
# input = sys.stdin.readline
#
#
# def info():
#     a, b = map(float, input().split())
#     a = int(a)
#     b = int(b * 100 + 0.5)
#     return a, b
#
#
# while True:
#     N, M = info()
#     if N == 0:
#         break
#
#     cals = []
#     prices = []
#
#     for _ in range(N):
#         c, p = info()
#         cals.append(c)
#         prices.append(p)
#
#     dp = [0] * 10001
#
#     for i in range(1, M+1):
#         for j in range(N):
#             cal = cals[j]
#             price = prices[j]
#
#             if i < price:
#                 continue
#
#             dp[i] = max(dp[i], dp[i-price] + cal)
#
#     print(dp[M])


# 시간 초과
# Pypy 제출 / 실수 -> 정수 시 0.5를 더해주어야 한다
import sys

input = sys.stdin.readline


# 정보를 필요한 정수 형태로 변경
def info():
    a, b = input().split()
    a = int(a)
    b = int(float(b) * 100 + 0.5)   # 100배하여 정수로 변환 / 0.5를 더해주어야 오류가 발생하지 않음
    return a, b


while True:
    N, M = info()

    # 종료 조건 확인
    if N == 0:
        break

    dp = [0 for _ in range(M + 1)]   # 총 금액 + 1개 초기화

    for _ in range(N):   # 사탕의 갯수만큼
        cal, price = info()   # 현재 사탕의 칼로리와 가격을 받아
        for j in range(price, M+1):   # 가격부터 최대 금액까지
            dp[j] = max(dp[j], dp[j-price] + cal)   # 현재 비용으로 먹을 수 있는 칼로리와, 이 사탕을 구매해서 먹을 수 있는 칼로리 중 큰 것 선택

    print(max(dp))
