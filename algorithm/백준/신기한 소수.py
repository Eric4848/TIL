N = int(input())


# 소수 확인하는 함수
def check(n):
    if n == 1:   # 입력이 1이면
        return False   # 소수아님

    for i in range(2, int(n ** 1/2) + 1):   # 2부터 자신의 루트까지
        if n % i == 0:   # 나누엇을 때 나누어 떨어지면
            return False   # 소수아님(2인경우 확인하지 않음)

    return True   # 소수


# dfs로 아래 숫자 확인
def dfs(num):
    if len(str(num)) == N:   # 입력 숫자의 길이가 주어진 것과 같다면
        print(num)   # 해당 숫자 출력

    else:   # 짧다면
        for i in range(10):   # 0 ~ 9까지
            now = num * 10 + i   # 오른쪽에 추가해서
            if check(now):   # 소수라면
                dfs(now)   # 그 숫자를 추가로 확인


# 시작 숫자별로 dfs진행(한자리 소수)
dfs(2)
dfs(3)
dfs(5)
dfs(7)

# 메모리 초과
# N = int(input())
# prime = [1] * 10 ** N
# prime[1] = 0
# for i in range(2, int((10 ** N) ** 1/2)):
#     if prime[i]:
#         for j in range(i ** 2, 10 ** N, i):
#             prime[j] = 0
#
# for i in range(10 ** (N-1), 10 ** N):
#     if prime[i]:
#         chk = 1
#         for j in range(1, N):
#             if not prime[i // (10 ** j)]:
#                 chk = 0
#                 break
#
#         if chk:
#             print(i)
