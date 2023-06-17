N = int(input())
houses = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N):
    houses[i][0] += min(houses[i-1][1], houses[i-1][2])
    houses[i][1] += min(houses[i-1][2], houses[i-1][0])
    houses[i][2] += min(houses[i-1][0], houses[i-1][1])

print(min(houses[-1]))

# N = int(input())
# houses = [list(map(int, input().split())) for _ in range(N)]
# dp1 = [[0] * 3 for _ in range(N)]
# dp2 = [[0] * 3 for _ in range(N)]
# dp1[0] = houses[0]
# dp2[0] = houses[0]
# print(dp1)
#
# for i in range(1, N):
#     dp1[i][1] = houses[i][1] + dp1[i-1][0]
#     dp1[i][2] = houses[i][2] + dp1[i-1][1]
#     dp1[i][0] = houses[i][0] + dp1[i-1][2]
#
# for i in range(1, N):
#     dp2[i][2] = houses[i][2] + dp2[i-1][0]
#     dp2[i][0] = houses[i][0] + dp2[i-1][1]
#     dp2[i][1] = houses[i][1] + dp2[i-1][2]
#
# answer1 = min(dp1[-1])
# answer2 = min(dp2[-1])
# print(dp1)
# print(dp2)
# if answer1 < answer2:
#     print(answer1)
# else:
#     print(answer2)
