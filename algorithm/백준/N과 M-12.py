n, length = map(int, input().split())
nums = list(map(int, input().split()))
nums = list(set(nums))
nums.sort()

answer = []
temp = []


def dfs(prev):
    if len(temp) == length:
        answer.append(temp[:])
        return
    for i in range(len(nums)):
        if nums[i] < prev:
            continue
        temp.append(nums[i])
        dfs(nums[i])
        temp.pop()


dfs(0)

for i in range(len(answer)):
    print(*answer[i])
