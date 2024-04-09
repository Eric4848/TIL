N, K = map(int, input().split())
nums = input().rstrip()
q = [nums[0]]   # 큐에 첫번째 숫자를 저장
for i in range(1, N):   # 두번째부터 마지막 숫자까지
    while q:   # 비교할 큐가 있으면
        if int(nums[i]) <= int(q[-1]) or K == 0:   # 큐의 마지막 숫자가 이번 숫자 이상이거나 더이상 뺄 수 없으면
            break   # 종료
        q.pop()   # 큐의 마지막 숫자 제거
        K -= 1   # 뺄 수 있는 숫자 - 1

    q.append(nums[i])   # 큐에 지금 숫자 추가

for _ in range(K):   # 뺄 수 있는 숫자 갯수만큼
    q.pop()   # 큐의 마지막 숫자 제거
print(''.join(q))
