N = int(input())
ins = input().rstrip()
nums = []   # 숫자를 담을 리스트
ops = []   # 연산자를 담을 리스트
answer = -float('inf')   # 정답을 무한소로 초기화
# 숫자, 연산자 분리
for i in range(N):
    if i % 2 == 0:
        nums.append(int(ins[i]))
    else:
        ops.append(ins[i])


# 연산자 별로 계산하는 함수
def calc(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b


# 괄호를 묶어 연산하는 함수
def dfs(idx, value):
    global answer
    # 마지막 숫자시작 계산이면
    if idx == N // 2:
        answer = max(answer, value)   # 정답에 정답과 여태까지 계산값중 큰 것 저장
        return

    # 다음 계산할 숫자가 있다면
    if idx+1 <= N // 2:
        nxt = calc(value, ops[idx], nums[idx+1])   # 현재값과 다음숫자에 연산대로 계산
        dfs(idx+1, nxt)   # 다음 숫자, 계산한 결과로 dfs

    # 다다음 계산할 숫자가 있다면
    if idx+2 <= N // 2:
        nxtnxt = calc(nums[idx+1], ops[idx+1], nums[idx+2])   # 다음 연산자에 괄호를 쳐 계산한 값 계산
        nxt = calc(value, ops[idx], nxtnxt)   # 현재 값과 다음 괄호 값 계산
        dfs(idx+2, nxt)   # 다다음 숫자, 계산한 결과로 dfs


dfs(0, nums[0])   # 0번인덱스, 0번 인덱스의 숫자로 dfs
print(answer)


# N = int(input())
# calcs = input().rstrip()
# answer = -float('inf')
# nums = []
# opers = []
# is_pri = [False for _ in range(N // 2)]
# if N == 1:
#     answer = int(calcs[0])
#
# for i in range(N):
#     if i % 2 == 0:
#         nums.append(int(calcs[i]))
#     else:
#         opers.append(calcs[i])
#
#
# def calc(M):
#     tmp = []
#     to = []
#     pre = False
#     for i in range(M):
#         if is_pri[i]:
#             if opers[i] == '+':
#                 tmp.append(nums[i] + nums[i+1])
#             elif opers[i] == '-':
#                 tmp.append(nums[i] - nums[i+1])
#             else:
#                 tmp.append(nums[i] * nums[i+1])
#             pre = True
#         else:
#             if pre:
#                 pre = False
#                 to.append(opers[i])
#             else:
#                 tmp.append(nums[i])
#                 to.append(opers[i])
#     if not pre:
#         tmp.append(nums[-1])
#     ret = tmp[0]
#     for i in range(len(to)):
#         if to[i] == '+':
#             ret += tmp[i+1]
#         elif to[i] == '-':
#             ret -= tmp[i+1]
#         else:
#             ret *= tmp[i+1]
#     return ret
#
#
# def dfs(num, n, m):
#     ret = -float('inf')
#     if n == m:
#         return calc(m)
#
#     if 0 < n and is_pri[n-1]:
#         ret = max(ret, dfs(num, n+1, m))
#     else:
#         t = dfs(num, n+1, m)
#         ret = max(ret, t)
#         is_pri[n] = True
#         t = dfs(num, n+1, m)
#         ret = max(ret, t)
#         is_pri[n] = False
#     return ret
#
#
# answer = dfs(N, 0, N//2)
# print(answer)
