codes = input()   # 암호를 입력받아
nums = [int(code) for code in codes]   # 각 자리를 숫자로 변경해서 리스트로 만들어준다
answer = [1, 1]   # 계산을 위해 1을 맨 앞에 넣어주고 첫자리가 0이 아닐경우를 가정하므로 1을 하나 더 추가한다
L = len(nums)

for i in range(1, L):   # 두번째부터 마지막 암호까지
    if nums[i] == 0:   # 현재 암호가 0이라면
        if nums[i-1] == 1 or nums[i-1] == 2:   # 그 앞자리 암호가 1이나 2인 경우
            answer[-1] = answer[-2]   # 정답을 현재 이전으로 변경한다(pop으로 제거해도 되지만 변경이 성능이 더 좋다)
        else:   # 앞자리가 그 외인 경우
            answer.append(0)   # 정답에 0을 추가한 후
            break   # 계산을 그만한다
    else:   # 현재 암호가 0이 아니라면
        answer.append(answer[-1])   # 이전 정답 만큼 현재 정답을 추가한다(이전 암호 + 현재 숫자)

        if nums[i-1] == 2:   # 이전 암호가 2인 경우
            if nums[i] <= 6:   # 현재 암호가 6 이하라면
                answer[-1] += answer[-3]   # 정답에 전전 정답을 더해준다(전전 암호 + 앞자리+현재숫자)

        if nums[i-1] == 1:   # 이전 암호가 1인경우
            answer[-1] += answer[-3]   # 마찬가지로 전전 정답을 더해준다

if nums[0] == 0:   # 암호가 0으로 시작하는 경우
    answer.append(0)   # 정답에 0을 추가한다

print(answer[-1] % 1000000)   # 마지막 값을 1000000으로 나눈 나머지를 출력한다


# 시간 초과
# import sys
#
# sys.setrecursionlimit(10 ** 9)
# codes = input()
# nums = [int(code) for code in codes]
# answer = [0]
# L = len(nums)
# 121074110
#
# def search(i):
#     if i == L:
#         answer[0] += 1
#         return
#
#     if nums[i] == 0:
#         return
#
#     search(i+1)
#
#     if nums[i] == 2:
#         if nums[i+1] < 7:
#             if i < L-1:
#                 search(i+2)
#
#     if nums[i] == 1:
#         if i < L-1:
#             search(i+2)
#
#
# search(0)
# print(answer[0] % 1000000)
