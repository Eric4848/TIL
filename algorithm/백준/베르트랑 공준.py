# 에라토스의 채 사용
maximum = 123456
eratos = [0] * 2 + [1] * maximum * 2   # 0~123456*2+1까지 0, 1은 0 나머지는 1로 에라토스의 채 생성
# 반드시 0부터 시작 -> 공차 계산을 위해 for문에서의 i인자를 사용하기 때문에 인덱스를 맞춰주어야 함
for i in range(2, 2 * maximum + 1):   # 2~123456*2까지
    if eratos[i]:   # 해당 수가 소수이면
        for j in range(i * 2, maximum * 2 + 1, i):   # 소수인 수 *2부터 소수만큼의 공차로 이동하며
            eratos[j] = 0   # 소수가 아니라고 바꿔준다

while True:
    n = int(input())
    if n == 0:
        break
    print(sum(eratos[n+1:n*2+1]))   # 입력값+1 부터 입력값의 2배까지의 합을 구한다(소수만 1이기 때문에)


# 시간초과
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     answer = 0
#     for i in range(n+1, 2*n + 1):
#         answer += 1
#         if i == 1:
#             answer -= 1
#         for j in range(2, int(i**0.5)+1):
#             if i % j == 0:
#                 answer -= 1
#                 break
#     print(answer)
