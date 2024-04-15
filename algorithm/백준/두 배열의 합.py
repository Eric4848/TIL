# Index Error(범위가 음수도 있음)
T = int(input())
NA = int(input())
A = list(map(int, input().split()))
TA = sum(A)+1
NB = int(input())
B = list(map(int, input().split()))
TB = sum(B)+1
answer = 0


tmpA = [0 for _ in range(max(A)+1)]
tmpB = [0 for _ in range(max(B)+1)]

for a in A:
    tmpA[a] += 1
for b in B:
    tmpB[b] += 1

dpA = [0 for _ in range(TA)]
dpB = [0 for _ in range(TB)]

A = set(A)
B = set(B)

for num in A:
    for i in range(1, TA - num):
        if dpA[i]:
            dpA[i+num] = dpA[i]
    dpA[num] += tmpA[num]

for num in B:
    for i in range(1, TB - num):
        if dpB[i]:
            dpB[i+num] = dpB[i]
    dpB[num] += tmpB[num]

for i in range(1, T):
    if NA < i or NB < T-i:
        continue
    answer += dpA[i] * dpB[T-i]

print(answer)


# 메모리 초과
# T = int(input())
# NA = int(input())
# LA = list(map(int, input().split()))
# A = set(LA)
# TA = sum(A)+1
# NB = int(input())
# LB = list(map(int, input().split()))
# B = set(LB)
# TB = sum(B)+1
# answer = 0
#
# dpA = [0 for _ in range(TA)]
# dpB = [0 for _ in range(TB)]
#
# tmpA = [0 for _ in range(max(LA)+1)]
# tmpB = [0 for _ in range(max(LB)+1)]
#
# for a in LA:
#     tmpA[a] += 1
# for b in LB:
#     tmpB[b] += 1
#
#
# for num in A:
#     for i in range(1, TA - num):
#         if dpA[i]:
#             dpA[i+num] = dpA[i]
#     dpA[num] += tmpA[num]
#
# for num in B:
#     for i in range(1, TB - num):
#         if dpB[i]:
#             dpB[i+num] = dpB[i]
#     dpB[num] += tmpB[num]
#
# for i in range(1, T):
#     if NA < i or NB < T-i:
#         continue
#     answer += dpA[i] * dpB[T-i]
#
# print(answer)
