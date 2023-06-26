N = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
print(dp[N])

# 시간 초과
# import sys
# sys.setrecursionlimit(10 ** 9)   # 재귀 깊이를 증가시킴
#
#
# def tile(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return tile(n-1) + tile(n-2)
#
#
# print(tile(int(input())) % 15746)

# 메모리 부족
# tiles = [0, 1, 2, 3]
# N = int(input())
# if 3 < N:
#     for _ in range(3, N):
#         tiles.append(tiles[-1]+tiles[-2])
# print(tiles[N] % 15746)
# 저장 값을 미리 나머지로 변경하면 가능
#         tiles.append((tiles[-1]+tiles[-2]) % 15746)
# print(tiles[N])
