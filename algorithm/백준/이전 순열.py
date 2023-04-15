num = int(input())
target = list(map(int, input().split()))
is_used = [False for _ in range(num)]
temp = []
prev = []


def dfs():
    if len(temp) == num:
        if temp == target:
            if not prev:
                print(-1)
            else:
                print(*prev[-1])
            return
        else:
            prev.append(temp[:])
        return

    for i in range(num):
        if not is_used[i]:
            temp.append(i + 1)
            is_used[i] = True
            dfs()
            temp.pop()
            is_used[i] = False


dfs()

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
