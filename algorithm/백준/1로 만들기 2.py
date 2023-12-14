N = int(input())
dp = [0 for i in range(N+1)]   # 계산 홧수를 0회로 초기화

for i in range(2, N+1):   # 2부터 N까지
    dp[i] = dp[i-1] + 1   # 현재 숫자에서 1까지 가는 계산 횟수는 이전 수 + 1(-1 계산 한 경우)

    if i % 2 == 0:   # 2로 나누어 떨어지면
        dp[i] = min(dp[i], dp[i//2] + 1)   # 현재 횟수와 2로 나눈 몫 + 1회중 작은 것 선택

    if i % 3 == 0:   # 3도 동일
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[N])   # N의 최소 계산 횟수 출력
nums = [N]   # 계산한 숫자들 리스트에 입력값 추가
now = N   # 현재 숫자를 입력값으로 초기화
count = dp[N] - 1   # 계산 횟수를 정답-1회로 설정

for i in range(N, 0, -1):   # 정답부터 1까지 역순으로
    if dp[i] == count and (i+1 == now or i*2 == now or i*3 == now):   # 해당 숫자의 계산 횟수와 현재 계산 횟수가 같고, 그 위치에서 계산 시 현재 숫자가 나온다면
        nums.append(i)   # 숫자 리스트에 현재 숫자 추가
        now = i   # 현재 숫자를 변경
        count -= 1   # 계산 횟수를 -1회
print(*nums)   # 숫자들 출력


# 시간 초과
# from collections import deque
#
# N = int(input())
# q = deque([[N]])
# while q:
#     nums = q.popleft()
#     now = nums[-1]
#     if now == 1:
#         print(len(nums)-1)
#         print(*nums)
#         break
#
#     if now % 3 == 0:
#         q.append(nums+[now // 3])
#
#     if now % 2 == 0:
#         q.append(nums+[now // 2])
#
#     q.append(nums + [now - 1])
