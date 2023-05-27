from collections import Counter

T = int(input())
nums = [int(input()) for _ in range(T)]
nums.sort()
counts = Counter(nums).most_common()

print(round(sum(nums)/T))
print(nums[T//2])
if len(counts) > 1 and counts[0][1] == counts[1][1]:
    print(counts[1][0])
else:
    print(counts[0][0])
print(nums[T-1]-nums[0])


# T = int(input())
# nums = []
# for _ in range(T):
#     nums.append(int(input()))
# nums.sort()
# sets = list(set(nums))
# sets.sort()
# counts = []
# maximum = 0
# for st in sets:
#     cnt = nums.count(st)
#     if cnt > maximum:
#         counts = [st]
#         maximum = cnt
#     elif cnt == maximum:
#         counts.append(st)
# print(counts)
# print(round(sum(nums)/T))
# print(nums[T//2])
# if len(counts) == 1:
#     print(counts)
# else:
#     print(counts[1])
# print(nums[T-1]-nums[0])
