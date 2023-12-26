import sys

sosu = set(i for i in range(2, 1000001))   # set을 사용해 범위 내 숫자들을 저장한다
for i in range(2, 1001):   # 2부터 범위의 루트값 만큼
    if i in sosu:   # 해당 숫자가 소수 set에 있으면
        sosu.difference_update(range(i * i, 1000001, i))   # 자신의 제곱부터 자신 간격으로 set에서 제거(set에서 숫자를 찾는 것이 빠르다, 자승 이전의 수는 앞에서 이미 제거 하였다)

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    wrong = True   # 추측이 틀렸다고 가정

    for small in sosu:   # 소수 집합의 작은 수부터
        if n - small in sosu:   # 입력 - 해당 소수가 소수에 있다면
            print(f'{n} = {small} + {n - small}')   # 출력하고
            wrong = 0   # 추측이 맞다고 변경
            break

    if wrong:   # 추측이 틀렸다면
        print("Goldbach's conjecture is wrong.")

# 시간 초과
# import sys
#
# sosu = {i: True for i in range(1000001)}
# for i in range(2, 1001):
#     if sosu[i]:
#         for j in range(2*i, 1000001, i):
#             sosu[j] = False
#
# while True:
#     n = int(sys.stdin.readline())
#     chk = 1
#
#     if n == 0:
#         break
#
#     for i in range(3, n // 2+1):
#         if sosu[i] and sosu[n-i]:
#             print(f'{n} = {i} + {n-i}')
#             chk = 0
#             break
#
#     if chk:
#         print("Goldbach's conjecture is wrong.")


# 시간 초과
# sosu = [True] * 1000001
# for i in range(2, 1001):
#     if sosu[i]:
#         for j in range(2*i, 1000001, i):
#             sosu[j] = False
#
# while True:
#     n = int(input())
#
#     if n == 0:
#         break
#
#     for i in range(3, n // 2):
#         if sosu[i] and sosu[n-i]:
#             print(f'{n} = {i} + {n-i}')
#             break
#         if i == n // 2:
#             print("Goldbach's conjecture is wrong.")
