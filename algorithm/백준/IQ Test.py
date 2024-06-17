N = int(input())
nums = list(map(int, input().split()))
# 주어진 숫자가 1개인 경우
if N == 1:
    print('A')   # 무수히 많음

# 주어진 숫자가 2개인 경우
elif N == 2:
    if nums[0] == nums[1]:   # 두 숫자가 같다면
        print(nums[0])   # 다음도 같은 숫자
    else:   # 다르다면
        print('A')   # 무수히 많음

# 주어진 숫자가 3개 이상인 경우
else:
    # a값 계산
    if nums[0] == nums[1]:   # 숫자1, 2가 같다면
        a = 0   # a = 0 (모두 같은 숫자인 경우 a = 1, b = 0과 a = 0, b = nums[0]가 가능)
    else:   # 숫자1, 2가 다르다면
        a = (nums[2]-nums[1]) // (nums[1]-nums[0])   # 숫자2, 3의 차를 숫자1, 2의 차로 나눈 몫 저장(정수조건)

    b = nums[1] - nums[0] * a   # b값 계산 / 2번째 숫자 - 1번째 숫자 * a

    # 규칙 검사
    for i in range(N-1):   # N - 1개쌍
        nxt = nums[i] * a + b   # 다음 수 예상
        if nxt != nums[i+1]:   # 예상값이 실제와 다르면
            print('B')   # 불가능 출력
            exit()   # 종료

    # 모든 예측값이 맞다면
    print(nums[-1] * a + b)   # 마지막 값에서 계산하여 출력


# 오답
# N = int(input())
# nums = list(map(int, input().split()))
# diff = []
# chk = 'P'
# if N == 1:
#     print('A')
#     exit()
#
# if N == 2 and nums[0] == nums[1]:
#     print(nums[0])
#     exit()
#
# if N == 2 and nums[0] != nums[1]:
#     print('A')
#     exit()
#
# for i in range(N-1):
#     diff.append(nums[i+1] - nums[i])
#
# if diff[0] == 0:
#     for i in range(N-1):
#         if diff[i] != 0:
#             print('B')
#             exit()
#     print(nums[0])
#     exit()
#
# a = diff[1] // diff[0]
#
# for i in range(N-2):
#     if diff[i] == 0:
#         print('B')
#         exit()
#     if diff[i+1] // diff[i] != a:
#         print('B')
#         exit()
#
# b = nums[1] - nums[0] * a
# for i in range(N-1):
#     if nums[i+1] - nums[i] * a != b:
#         print('B')
#         exit()
#
# print(nums[-1] * a + b)
