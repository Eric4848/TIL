N = int(input())
nums = [1 for _ in range(N+1)]
sosu = [0]
answer = 0
for i in range(2, int(N ** 0.5) + 1):
    if nums[i]:
        for j in range(i ** 2, N+1, i):
            nums[j] = 0

for i in range(2, N+1):
    if nums[i]:
        sosu.append(i)

for i in range(1, len(sosu)):
    sosu[i] += sosu[i-1]

left = 0
right = 1

while right < len(sosu):
    now = sosu[right] - sosu[left]
    if now < N:
        right += 1
    elif N < now:
        left += 1
    else:
        answer += 1
        left += 1

print(answer)


# 시간 초과
# N = int(input())
# nums = [1 for _ in range(N+1)]
# nums[1] = 0
# sosu = []
# answer = 0
# for i in range(2, int(N ** 0.5) + 1):
#     for j in range(i ** 2, N+1, i):
#         nums[j] = 0
#
# for i in range(2, N+1):
#     if nums[i]:
#         sosu.append(i)
#
# if sosu[-1] == N:
#     answer += 1
#
# for i in range(1, len(sosu)):
#     sosu[i] += sosu[i-1]
#
# for e in range(len(sosu)):
#     if sosu[e] == N:
#         answer += 1
#     for s in range(e-1):
#         if sosu[e] - sosu[s] < N:
#             break
#         if sosu[e] - sosu[s] == N:
#             answer += 1
#
# print(answer)
