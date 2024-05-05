import sys

input = sys.stdin.readline
K = int(input())
stack = []   # 숫자를 담을 스택
for _ in range(K):
    num = int(input())
    if num == 0:   # 숫자가 0이면
        stack.pop()   # 마지막 숫자 제거(무조건 제거 가능 조건)
    else:   # 0이 아니면
        stack.append(num)   # 해당 숫자를 스택에 추가

print(sum(stack))   # 스택에 쌓인 숫자들을 더하여 출력
