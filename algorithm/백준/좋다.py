N = int(input())
nums = list(map(int, input().split()))
nums.sort()   # 숫자들을 정렬한다
answer = 0   # 정답을 0으로 초기화
if 2 < N:   # 숫자가 3개 이상 있으면
    for i in range(N):   # 모든 숫자에 대해
        goal = nums[i]   # 해당 숫자를 목표로 설정
        f = 0   # 제일 작은 숫자
        e = N-1   # 제일 큰 숫자
        while f < e:   # 같은 수를 사용하지 않기 때문에 작은 수가 큰수보다 작은 경우
            if f == i:   # 작은 수가 목표 숫자라면
                f += 1   # 작은 수를 다음 수로 만들고
                continue   # 다시 진행
            if e == i:   # 큰 수의 경우도 동일하다
                e -= 1
                continue

            added = nums[f] + nums[e]   # 작은 수와 큰 수를 더한 값
            if added == goal:   # 더한 값이 목표값이라면
                answer += 1   # 정답을 1개 늘리고
                break   # 종료한다
            if added < goal:   # 합이 목표보다 작은 경우
                f += 1   # 작은 수를 하나 키운다
            else:   # 합이 목표보다 큰 경우
                e -= 1   # 큰 수를 하나 줄인다
print(answer)


# 시간 초과
# N = int(input())
# nums = list(map(int, input().split()))
# nums.sort()
# answer = 0
# for i in range(2, N):
#     chk = 0
#     for a in range(0, i-1):
#         if chk:
#             break
#         for b in range(i-1, a, -1):
#             if nums[a] + nums[b] == nums[i]:
#                 answer += 1
#                 chk = 1
#                 break
#
# print(answer)


# 시간 초과
# N = int(input())
# nums = list(map(int, input().split()))
# answer = 0
# for i in range(2, N):
#     chk = 0
#     for j in range(0, i):
#         if chk:
#             break
#         for k in range(j, i):
#             if j != k:
#                 if nums[j] + nums[k] == nums[i]:
#                     answer += 1
#                     chk = 1
#                     break
# print(answer)
