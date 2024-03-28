# 다른 풀이
dp = [1 for _ in range(10001)]   # 범위+1만큼 1로 초기화

# 가짓수에 2를 하나씩 추가한다
for i in range(2, 10001):
    dp[i] += dp[i-2]   # 현재 경우의 수에 2만큼 적은 경우의 수를 더해준다

# 가짓수에 3을 하나씩 추가한다
for i in range(3, 10001):
    dp[i] += dp[i-3]   # 현재 경우의 수에 3만큼 적은 경우의 수를 더해준다

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N])


# # 첫번째 행은 1,두번째, 세번째 행은 0으로 초기화
# dp = [[1 for i in range(10001)], [0 for i in range(10001)], [0 for i in range(10001)]]
# dp[0][0] = 0   # 첫행의 0위치를 0으로 설정
# dp[1][2] = 1   # 둘째행의 2위치를 1로 설정
# dp[2][3] = 1   # 셋째행의 3위치를 1로 설정
#
# # 2 기준으로 만들 수 있는 경우 계산
# for c in range(3, 10001):   # 3부터 (2인경우 1개 설정 했으므로)
#     dp[1][c] += dp[0][c-2] + dp[1][c-2]   # 1, 2로 만들 수 있는 숫자들 중 2 적은 수의 가짓수를 더해준다
#
# # 1, 2로 만들 수 있는 가짓수 더하기
# for c in range(10001):
#     dp[1][c] += dp[0][c]
#
# # 3 기준으로 만들 수 있는 경우 계산
# for c in range(4, 10001):   # 4부터(3인경우 1개 설정했으므로)
#     dp[2][c] += dp[1][c-3] + dp[2][c-3]   # 1,2/ 3으로 만들 수 있는 숫자들 중 3 적은 수의 가짓수를 더해준다
#
# # 1,2/ 3으로 만들 수 있는 가짓수 더하기
# for c in range(10001):
#     dp[2][c] += dp[1][c]
#
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     print(dp[2][N])


# dp = [[1 for _ in range(10001)], [i // 2 if i % 2 == 0 else 0 for i in range(10001)], [i // 3 if i % 3 == 0 else 0 for i in range(10001)]]
# for r in range(3):
#     dp[r][0] = 0
#
# for c in range(2, 10001):
#     if dp[1][c] == 0:
#         dp[1][c] = dp[1][c-1]
#     else:
#         dp[1][c] += dp[0][c-2]
#
# for c in range(3, 10001):
#     if dp[2][c] == 0:
#         dp[2][c] = dp[2][c-1] + dp[1][c-3]
#     else:
#         dp[2][c] += dp[0][c-3] + dp[1][c-3]
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     print(dp[2][N] + dp[1][N] + dp[0][N])
#
# for d in dp:
#     print(*d)


# dp = [[1 for _ in range(10001)], [1 if i % 2 == 0 else 0 for i in range(10001)], [1 if i % 3 == 0 else 0 for i in range(10001)]]
# for r in range(3):
#     dp[r][0] = 0
#
# for c in range(2, 10001):
#     dp[1][c] += dp[0][c-2] + dp[1][c-2]
#
# for c in range(3, 10001):
#     dp[2][c] += dp[0][c-3] + dp[1][c-3] + dp[2][c-3]
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     print(dp[2][N])
#
# for d in dp:
#     print(*d)
