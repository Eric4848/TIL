N = int(input())
nums = list(map(int, input().split()))[1:]   # 조건을 제외한 나머지(1 1, 2 1인 경우 정답이 같으므로 길이로 판단 가능)
orders = [i+1 for i in range(N)]   # 원본 순서
factos = []   # 팩토리얼을 역순으로 저장할 리스트(위치 변경 순서때문)
for i in range(N-1, 0, -1):   # N - 1개의 역순으로
    tmp = 1   # 팩토리얼의 기본 값 1
    for j in range(2, i+1):   # 2부터 팩토리얼 목표번째수까지
        tmp *= j   # 곱해준다
    factos.append(tmp)   # 값을 팩토리얼 리스트에 저장

# 조건 1
if len(nums) == 1:   # 조건 길이가 1인경우
    answer = []   # 정답을 저장할 리스트
    idxs = []   # 팩토리얼 인덱스별 변경 수
    calc = nums[0] - 1   # 계산할 값(바뀌는 위치의 값 -> 원본은 그대로)

    # 팩토리얼 별 이동 수 계산
    for facto in factos:   # 팩토리얼 별로
        idxs.append(calc // facto)   # 계산할 값을 팩토리얼로 나눈 값 저장(팩토리얼 가짓수 만큼 뒷칸 수자를 옮김)
        calc %= facto   # 계산할 값을 팩토리얼로 나눈 나머지로 변경

    # 정답 계산
    for idx in idxs:   # 팩토리얼 위치별로
        answer.append(orders[idx])   # 팩토리얼 번쨰의 값만큼 뒤의 숫자 저장
        orders = orders[:idx] + orders[idx+1:]   # 해당 숫자를 뺀 나머지로 변경
    answer += orders   # 마지막에 남은 숫자 더해준다
    print(*answer)

# 조건 2
else:
    # 옮겨진 숫자들의 위치별 거리 계산
    idxs = []   # 당겨진 위치별 거리를 저장할 리스트
    while nums:   # 입력된 숫자만큼
        num = nums[0]   # 처음 숫자를 가져온다
        nums = nums[1:]   # 가져온 숫자 제거
        for idx, order in enumerate(orders):   # 순서의 인덱스와 값을 돌며
            if order == num:   # 가져온 숫자와 같다면
                idxs.append(idx)   # 당겨진 수에 해당 순서의 인덱스 저장
                orders.remove(order)   # 저장한 순서 제거
                break   # 종료
    answer = 1   # 정답을 1로 초기화(원본이 1부터)

    # 정답 계산
    for i in range(N-1):
        answer += idxs[i] * factos[i]   # 당겨진 위치의 거리만큼 팩토리얼을 곱해서 정답에 추가
    print(answer)
