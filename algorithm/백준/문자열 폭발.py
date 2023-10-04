import sys

input = sys.stdin.readline
F = input()[:-1]   # readline으로 입력받는경우 맨뒤에 \n이 추가된다
S = input().strip()   # strip을 사용하면 없이 입력받을 수 있다
L = len(S)
stack = []   # 스택을 초기화 한다
for i in range(len(F)):
    stack.append(F[i])   # 스택에 한글자씩 넣으면서
    if ''.join(stack[-L:]) == S:   # 스택의 맨 뒤 문자들이 폭파 문자열과 같으면
        for _ in range(L):   # 폭파 문자열 수만큼
            stack.pop()   # 스택에서 pop해준다
if stack:
    print(''.join(stack))
else:
    print('FRULA')


# type_error
# import sys
#
# input = sys.stdin.readline
# F = input().strip()
# S = input().strip()
# stack = []
# temp = []
# for i in range(len(F)):
#     stack.append(F[i])
#     if stack and stack[-1] == S[-1] and len(S) <= len(stack):
#         temp += stack.pop()
#         for j in range(1, len(S)):
#             if stack[-1] != S[-1-j]:
#                 stack += temp.reverse()
#                 temp = []
#                 continue
#             temp += stack.pop()
#             if j == len(S)-1:
#                 temp = []
#                 break
# if stack:
#     print(''.join(stack))
# else:
#     print('FRULA')


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# F = input()[:-1]
# S = input()[:-1]
#
# flag = 1
# while flag and F:
#     for i in range(len(F)):
#         if F[i] == S[0]:
#             chk = 0
#             for j in range(1, len(S)):
#                 if F[i+j] != S[j]:
#                     chk = 1
#                     break
#             if chk:
#                 continue
#             F = F[0:i] + F[i+len(S):]
#             break
#         if i == len(F)-1:
#             flag = 0
# if F:
#     print(F)
# else:
#     print('FRULA')
