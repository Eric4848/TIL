import sys

input = sys.stdin.readline
N = int(input())
nums = [0]   # 인덱스 위치를 위해 0으로 초기화
idxs = [False] * (N+1)   # 사용된 번호의 인덱스를 False로 초기화(위치를 맞추기 위해 N+1)
answer = []
for i in range(N):
    nums.append(int(input()))


# 원을 이루는지 확인하는 함수
def check(tmp):
    global answer
    if nums[tmp[-1]] == tmp[0]:   # 현제 인덱스의 번호와 시작 번호가 같으면
        answer += tmp   # 정답 리스트에 현재까지 숫자들을 저장하고
        for n in tmp:   # 각 번호별로
            idxs[n] = True   # 사용했다고 표시
        return   # 종료

    if nums[tmp[-1]] in tmp:   # 시작으로 돌아가지 않고 이미 나온 숫자가 있다면
        return   # 종료

    check(tmp + [nums[tmp[-1]]])   # 다음 숫자를 더해서 확인


for i in range(1, N+1):   # 인덱스별로
    if idxs[i]:   # 이미 원을 이루었으면
        continue   # 넘어간다
    check([i])   # 아닌경우 확인

answer.sort()
print(len(answer))
for a in answer:
    print(a)


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# N = int(input())
# nums = [0]
# answer = [0]
# for _ in range(N):
#     nums.append(int(input()))
#
# idxs = [False] * (N+1)
# includes = [False] * (N+1)
#
#
# def check(i, d):
#     global answer
#     if d == N:
#         if idxs == includes:
#             if len(answer) < sum(idxs):
#                 tmp = []
#                 for i in range(N+1):
#                     if idxs[i]:
#                         tmp.append(i)
#                 answer = tmp
#         return
#
#     idxs[i] = True
#     includes[nums[i]] = True
#     check(i+1, d+1)
#     idxs[i] = False
#     includes[nums[i]] = False
#     check(i+1, d+1)
#
#
# check(1, 0)
#
# print(len(answer))
# for a in answer:
#     print(a)
