import math

A, B = map(int, input().split())
answer = []
for _ in range(math.gcd(A, B)):   # 입력된 두 수의 최대 공약수 만큼
    answer += '1'   # 정답에 1을 늘려준다
print(''.join(answer))
