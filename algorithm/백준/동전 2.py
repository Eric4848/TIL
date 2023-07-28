n, k = map(int, input().split())
answers = [float('inf')] * (k+1)   # k를 만드는 최소 동전 개수를 무한으로 초기화 한다
nums = []   # 동전들의 크기를 저장할 리스트

for _ in range(n):
    num = int(input())   # 동전의 크기를 입력받아
    if num <= k:   # 동전의 크기가 목표 금액보다 작거나 같으면
        answers[num] = 1   # 해당 금액까지 필요한 동전 갯수를 1개로 변경하고
        nums.append(num)   # 가지고있는 동전 리스트에 추가한다

nums.sort()   # 같은 동전 제거

for i in range(1, k+1):   # k까지 점차 증가하며
    for num in nums:   # 가지고 있는 동전들중에
        if 0 < i - num:   # 현재 금액에서 그 동전을 빼도 양수인 경우
            if answers[i - num] + 1 < answers[i]:   # 현재 그 금액을 만드는 동전수보다 동전을 추가하는게 더 적은 동전인 경우
                answers[i] = answers[i - num] + 1   # 현재 금액의 필요 동전수를 변경한다

if answers[k] == float('inf'):   # 목표금액을 만들지 못하는 경우
    print(-1)   # -1을 출력한다
else:
    print(answers[k])
