import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
answer = 1   # 안증ㄹ 수 있는 방법을 1개로 초기화

cnts = [1, 1, 2]   # 연달아 앉은 일반 좌석의 앉을 수 있는 가지수를 1, 1, 2로 초기화한다(일반좌석 0개, 1개, 2개)
for i in range(2, N):   # N자리까지 연달은 좌석 추가
    cnts.append(cnts[i] + cnts[i-1])   # 이전까지 연속좌석 + 2개 전까지 연속좌석을 저장한다

nums = [0]   # 연달은 좌석 계산을 위해 VIP좌석 리스트를 0으로 초기화
for _ in range(M):
    nums.append(int(input()))   # VIP좌석들을 추가하고
nums.append(N+1)   # N+1 추가(계산용)

for i in range(M+1):   # 일반자리 계산
    answer *= cnts[nums[i+1] - nums[i] - 1]   # VIP좌석들 사이 일반좌석의 갯수의 경우의 수를 정답에 곱해준다

print(answer)

# 2 3 5 8 13
