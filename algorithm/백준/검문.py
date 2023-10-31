import sys
import math   # 최대 공약수 사용을 위해

input = sys.stdin.readline
N = int(input())
nums = [int(input()) for _ in range(N)]   # 숫자들을 입력받고
nums.sort()   # 오름차순으로 정렬한다
temp = [nums[i]-nums[i-1] for i in range(1, N)]   # 숫자간의 차를 저장하고
gcd = temp[0]   # 가장 작은 수를 최대공약수로 저장한다

for i in range(1, N-1):   # 나머지 차이들에서
    gcd = math.gcd(gcd, temp[i])    # 최대공약수를 구해 갱신한다

answers = set([gcd])   # 같은 숫자는 하나만 저장하기 위해 set으로 gcd를 저장한다
for i in range(2, int(gcd ** 0.5) + 1):   # 최대공약수의 1이 아닌 약수들을 구한다(최대공약수의 제곱근 아래 숫자들에 대해)
    if gcd % i == 0:   # 약수라면
        answers.add(i)   # 약수와
        answers.add(gcd // i)   # 최대 공약수를 약수로 나눈 수를 정답에 추가한다

print(*sorted(list(answers)))   # 정답을 리스트로 만들고 정렬하여 출력한다


# 시간 초과
# N = int(input())
# nums = [int(input()) for _ in range(N)]
# minimum = min(nums)
# answers = []
# for div in range(2, minimum):
#     rest = minimum % div
#     chk = 1
#     for num in nums:
#         if rest != num % div:
#             chk = 0
#     if chk:
#         answers.append(div)
# print(*answers)
