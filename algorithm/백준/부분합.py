N, S = map(int, input().split())
nums = list(map(int, input().split()))
H = 0   # 앞쪽 숫자의 위치
T = 0   # 뒷쪽 숫자의 위치
L = N+1   # 만족하는 길이를 N+1로 초기화(전체의 합이 답인 경우 N이 나올 수 있다)
total = nums[0]   # 합을 첫번째 숫자로 초기화

while H <= T:   # 뒷쪽 위치가 같거나 크다면
    if S <= total:   # 합이 정답 조건을 만족하는 경우
        L = min(L, T - H + 1)   # 정답과 현재 두 위치의 차 + 1을 비교하여 작은 것을 저장
        total -= nums[H]   # 합에서 앞쪽 숫자를 빼고
        H += 1   # 앞쪽 숫자의 위치를 하나 뒤로 미룬다
    else:   # 합이 정답 조건을 만족하지 못하는 경우
        T += 1   # 뒷쪽 숫자의 위치를 하나 뒤로 미룬다
        if T < N:   # 미룬 위치가 숫자들 범위 이내라면
            total += nums[T]   # 합에 그 숫자를 더해준다
        else:   # 범위를 벗어나면
            break   # 중단한다

if L == N+1:   # 합이 정답 조건을 만족하지 못하는 경우
    print(0)   # 0을 출력
else:   # 정답 조건을 만족하면
    print(L)   # 정답 출력


# 오답
# N, S = map(int, input().split())
# nums = list(map(int, input().split()))
# answer = N + 1
# total = sum(nums)
# H = 0
# T = N-1
# while S <= total:
#     if nums[H] < nums[T]:
#         total -= nums[H]
#         H += 1
#         answer -= 1
#     else:
#         total -= nums[T]
#         T -= 1
#         answer -= 1
# print(answer)


# 시간 초과
# N, S = map(int, input().split())
# nums = list(map(int, input().split()))
# answer = N
#
# for i in range(N):
#     total = 0
#     for j in range(i, N):
#         total += nums[j]
#         if S <= total:
#             answer = min(answer, j-i+1)
#             break
# print(answer)
