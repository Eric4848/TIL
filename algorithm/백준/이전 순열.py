n = int(input())
a = list(map(int, input().split()))
b = 0

for i in range(n - 1, 0, -1):
    if a[i - 1] > a[i]:
        target = i - 1
        break
else:
    b = 1
    print(-1)

if b == 0:
    for i in range(n - 1, 0, -1):
        if a[i] < a[target]:
            a[i], a[target] = a[target], a[i]
            break

    a = a[:target + 1] + sorted(a[target + 1:], reverse=True)
    print(*a)


# num = int(input())
# target = list(map(int, input().split()))
# temp = []
#
# for i in range(num):
#     last = target.pop()
#     if len(target) == 0:
#         print('-1')
#         break
#     if last < target[-1]:
#         temp.append(last)
#         temp.append(target.pop())
#         temp.sort(reverse=True)
#         for num in temp:
#             if num < last:
#                 temp.remove(num)
#                 target.append(num)
#                 temp.sort()
#                 target += temp
#                 break
#         temp.sort()
#         target += temp
#         break
#     temp.append(last)
#
# print(*target)


# num = int(input())
# target = list(map(int, input().split()))
# is_used = [False for _ in range(num)]
# temp = []
# prev = []
#
#
# def dfs():
#     if len(temp) == num:
#         if temp == target:
#             if not prev:
#                 print(-1)
#             else:
#                 print(*prev[-1])
#             return
#         else:
#             prev.append(temp[:])
#         return
#
#     for i in range(num):
#         if not is_used[i]:
#             temp.append(i + 1)
#             is_used[i] = True
#             dfs()
#             temp.pop()
#             is_used[i] = False
#
#
# dfs()

# from itertools import permutations
#
# num = int(input())
# target = list(map(int, input().split()))
# prev = []
# for perm in permutations(range(1, num + 1), num):
#     if perm == tuple(target):
#         if not prev:
#             print(-1)
#         else:
#             print(*prev)
#             break
#     prev = []
#     for i in perm:
#         prev.append(i)
