# 시간 초과
from collections import deque
from itertools import combinations

N, C = map(int, input().split())
thouses = []
for _ in range(N):
    thouses.append(int(input()))
thouses.sort()
houses = deque(thouses)
maximum = houses.pop()
minimum = houses.popleft()
answer = []
for combs in combinations(houses, C-2):
    temp = []
    combs = [minimum] + list(combs) + [maximum]
    for i in range(len(combs)-1):
        temp.append(combs[i+1] - combs[i])
    answer.append(min(temp))
print(max(answer))


# 시간 초과
# from itertools import combinations
#
# N, C = map(int, input().split())
# houses = []
# for _ in range(N):
#     houses.append(int(input()))
# houses.sort()
# answer = []
# for combs in combinations(houses, C):
#     temp = []
#     for i in range(len(combs)-1):
#         temp.append(combs[i+1] - combs[i])
#     answer.append(min(temp))
# print(max(answer))
