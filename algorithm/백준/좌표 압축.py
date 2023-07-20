import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
indexs = sorted(set(nums))   # 중복을 제거한 후 오름차순 정렬을 한다
index_dict = {indexs[i]: i for i in range(len(indexs))}   # 정렬한 숫자를 인덱스로 하여 제일 작은 수 부터 0 ~ 정렬숫자 갯수-1까지 저장한다
for i in nums:   # 전체 숫자에서
    print(index_dict[i], end=" ")   # 해당 숫자를 검색해서 값을 출력해준다(dict로 저장하여 속도가 O(1)이다)


# 시간 초과
# import sys
# input = sys.stdin.readline
# N = int(input())
# nums = list(map(int, input().split()))
# indexs = set(nums)
# indexs = sorted(indexs)
# for i in range(N):
#     for j in range(len(indexs)):   # 속도가 O(N) -> 시간 초과
#         if nums[i] == indexs[j]:
#             nums[i] = j
#             break
#
# print(*nums)
