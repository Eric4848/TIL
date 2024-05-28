A, B = map(int, input().split())
C = int(B ** 0.5)   # B의 루트값을 C로 저장(소수점 버림 -> 올리면 제곱 시 B를 넘어감)
primes = [1] * (C+1)   # C번 인덱스까지 소수라고 초기화
primes[0] = 0   # 0과
primes[1] = 0   # 1을 소수 아님으로 변경
nums = []   # 소수들을 저장할 리스트
answer = 0   # 정답 초기화
# 소수 검색
for i in range(2, C+1):   # 2부터 C번 인덱스까지
    if primes[i]:   # 소수라면
        nums.append(i)   # 저장
        for j in range(i*i, C+1, i):   # 현재 수의 제곱부터 C까지 현재 수 간격으로
            primes[j] = 0   # 소수가 아님
# 거의 소수 판별
for num in nums:   # 소수별로
    # 거의 소수 생성
    tmp = num * num
    # 최소 조건
    while tmp < A:   # 최소조건보다 작으면
        tmp *= num   # 현재 소수를 곱해준다
    # 최대 조건
    while tmp <= B:   # 최대조건 이하라면
        answer += 1   # 정답을 1늘리고
        tmp *= num   # 현재 소수를 곱해준다
print(answer)
