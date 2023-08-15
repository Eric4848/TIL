N = int(input())
nums = list(map(int, input().split()))
total = int(input())
minimum = 0   # 최솟값
maximum = max(nums)   # 최댓값

while minimum <= maximum:   # 이분탐색
    summary = 0   # 예산값의 합을 저장하기 위해 초기화
    mid = (minimum + maximum) // 2   # 최소, 최대값의 중간값
    for i in range(N):   # 각 예산마다
        if nums[i] < mid:   # 중간값보다 적게 필요하면
            summary += nums[i]   # 예산을 더하고
        else:   # 아니면
            summary += mid   # 중간값을 더한다
    if summary <= total:   # 총 예산값이 제한보다 작으면
        minimum = mid + 1   # 최솟값을 중간값 + 1로 설정한다
    else:   # 반대의 경우
        maximum = mid - 1   # 최댓값을 중간값 - 1로 설정한다

print(maximum)
