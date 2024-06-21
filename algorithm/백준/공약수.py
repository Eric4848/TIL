import math   # 최소 공배수 계산용

nums = list(map(int, input().split()))   # 최대 공약수, 최소 공배수 입력
to_div = nums[1] // nums[0]   # 두 수의 곱 = 최대 공약수와 최소 공배수의 곱이므로 각자 고유한 수의 곱 계산
tmp = int(to_div ** 0.5)   # 임시 값으로 계산한 수의 루트 값(버림)
while True:
    if to_div % tmp == 0:   # 고유 수의 곱이 임시값으로 나누어 떨어지면
        # 나눈 몫과 임시값의 최대 공약수가 1인지 확인(최소 공배수가 주어졌으므로)
        if math.lcm(tmp, to_div // tmp) == tmp * (to_div // tmp):
            print(tmp * nums[0], (to_div // tmp) * nums[0])   # 맞다면 최대 공약수를 곱해서 출력
            break   # 종료
    tmp -= 1   # 임시값을 1 줄인다
