import sys
from collections import defaultdict

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
counts = defaultdict(int)   # 숫자별 갯수를 저장할 딕셔너리
stack = []   # 스택을 초기화
answers = [-1] * N   # 정답을 -1로 초기화

# 갯수 저장
for num in nums:
    counts[num] += 1   # 숫자별로 1개씩 증가

# 큰 경우 계산
for i in range(N):
    while stack and counts[nums[stack[-1]]] < counts[nums[i]]:   # 스택이 있고 스택의 맨 뒤 위치의 갯수가 현재 값보다 작은 경우
        answers[stack.pop()] = nums[i]   # 스택에서 pop하여 해당 위치에 현재 숫자 저장
    stack.append(i)   # 현재 위치 스택에 저장

print(*answers)


# import sys
# from collections import defaultdict
#
# input = sys.stdin.readline
# N = int(input())
# nums = list(map(int, input().split()))
# counts = defaultdict(int)
# rights = []
# answers = []
# for num in nums:
#     counts[num] += 1
#
# for i in range(N-1, -1, -1):
#     chk = 0
#     cnt = counts[nums[i]]
#     for j in range(len(rights)-1, -1, -1):
#         if cnt < counts[rights[j]]:
#             answers.append(rights[j])
#             chk = 1
#             break
#     if not chk:
#         answers.append(-1)
#     rights.append(nums[i])
#
# print(*reversed(answers))
