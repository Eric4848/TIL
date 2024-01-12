N = int(input())
nums = list(map(int, input().split()))
diff = float('inf')   # 두 용액을 섞었을 떄 0과의 차이를 무한으로 초기화
front = 0   # 앞
back = N-1   # 뒤
while front < back:   # 앞, 뒤의 순서가 바뀌지 않을 때 까지(같아질 때 까지)
    mixed = nums[front] + nums[back]   # 혼합 용액의 값
    if abs(mixed) < diff:   # 혼합 용액의 값이 기존보다 0에 가까우면
        diff = abs(mixed)   # 기존 용액을 바꿔주고
        answers = [nums[front], nums[back]]   # 정답을 해당 위치로 저장한다

    if 0 < mixed:   # 혼합 용액이 양수라면
        back -= 1   # 양의 값을 줄여준다
    else:   # 음수라면
        front += 1   # 음의 값(절댓값)을 줄여준다

print(*answers)
