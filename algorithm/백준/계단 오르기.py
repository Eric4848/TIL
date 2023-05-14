n = int(input())

stairs = [int(input()) for _ in range(n)]
dp = [0]*n

if len(stairs) < 3:
    print(sum(stairs))

else:
    dp[0] = stairs[0]
    dp[1] = stairs[1] + stairs[0]
    for i in range(2, n):
        dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])
    print(dp[n-1])


# n = int(input())
#
# stairs = []
# for _ in range(n):
#     stairs.append(int(input()))
#
# stairs.reverse()
# answer = stairs[0]
# cnt = 1
#
# for i in range(1, n-1):
#     if cnt == 0:
#         answer += stairs[i]
#         cnt = 1
#
#     elif cnt == 1:
#         if stairs[i] < stairs[i+1]:
#             cnt = 0
#         else:
#             answer += stairs[i]
#             cnt = 2
#
#     elif cnt == 2:
#         cnt = 0
#
# if cnt != 2:
#     answer += stairs[n-1]
#
# print(answer)
