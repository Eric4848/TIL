n = int(input())
nums = []
temp = []
for _ in range(n):
    nums.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(nums[i])):
        if j == 0:
            temp.append(nums[i][0] + nums[i-1][0])
        elif j == len(nums[i]) - 1:
            temp.append(nums[i][j] + nums[i-1][j-1])
        else:
            if nums[i-1][j-1] > nums[i-1][j]:
                temp.append(nums[i][j] + nums[i-1][j-1])
            else:
                temp.append(nums[i][j] + nums[i-1][j])
    nums[i] = temp[:]
    temp = []

# for num in nums:
#     print(*num)
print(max(nums[n-1]))
