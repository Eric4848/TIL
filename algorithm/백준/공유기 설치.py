# 이분탐색을 사용해서 시간을 단축해야 한다
n, c = map(int, input().split())
nums = []
for i in range(n):
    nums.append(int(input()))
nums.sort()


def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2   # 최소거리와 최대 거리의 중간값을 기준으로 정함
        current = array[0]   # 현재 위치를 첫집으로 설정
        count = 1   # 설치한 공유기 갯수를 1개로 설정

        for i in range(1, len(array)):   # 두번째부터 나머지 집들까지
            if array[i] >= current + mid:   # 기준값보다 거리가 더 먼 경우
                count += 1   # 설치하고
                current = array[i]   # 현재 위치를 변경한다

        if count >= c:   # 공유기가 기준보다 많이 설치되면
            global answer
            start = mid + 1   # 최소거리를 중간값보다 1 키워주고
            answer = mid   # 정답을 기준거리로 저장한다
        else:   # 기준보다 적게 설치되면
            end = mid - 1   # 최대거리를 중간값보다 1줄여준다


start = 1   # 최소거리
end = nums[-1] - nums[0]   # 최대거리를 맨 뒤와 맨 앞집의 차이로 저장한다
answer = 0

binary_search(nums, start, end)
print(answer)

# 시간 초과
# from collections import deque
# from itertools import combinations
#
# N, C = map(int, input().split())
# thouses = []
# for _ in range(N):
#     thouses.append(int(input()))
# thouses.sort()
# houses = deque(thouses)
# maximum = houses.pop()
# minimum = houses.popleft()
# answer = []
# for combs in combinations(houses, C-2):
#     temp = []
#     combs = [minimum] + list(combs) + [maximum]
#     for i in range(len(combs)-1):
#         temp.append(combs[i+1] - combs[i])
#     answer.append(min(temp))
# print(max(answer))


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
