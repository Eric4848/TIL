# 시간 초과
N = int(input())
nums = [int(input()) for _ in range(N)]
minimum = min(nums)
answers = []
for div in range(2, minimum):
    rest = minimum % div
    chk = 1
    for num in nums:
        if rest != num % div:
            chk = 0
    if chk:
        answers.append(div)
print(*answers)
