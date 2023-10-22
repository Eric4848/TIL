txts = list(input())

stack = []   # 괄호들을 담아 둘 리스트
answer = 0   # 정답을 0으로 초기화
tmp = 1   # 앞에서부터 곱하기 연산을 하기 위해 1로 초기화

for i in range(len(txts)):

    if txts[i] == "(":   # 2가 곱해지는 괄호의 경우
        stack.append(txts[i])   # 괄호 리스트에 담아주고
        tmp *= 2   # 임시값에 2를 곱해준다

    elif txts[i] == "[":   # 3이 곱새지는 괄호의 경우
        stack.append(txts[i])   # 2배와 같다
        tmp *= 3

    elif txts[i] == ")":   # 2배를 닫는 괄호의 경우
        if not stack or stack[-1] == "[":   # 여는 괄호가 없거나 3배를 여는 괄호와 만날 경우
            answer = 0   # 정답을 0으로 초기화 하고
            break   # 중단한다
        if txts[i-1] == "(":   # 바로 전이 2배를 여는 괄호였을 경우
            answer += tmp   # 임시값을 더해준다(여태까지 곱해진 값들 * 2의 값이기 때문에)
        stack.pop()   # 2배 여는 괄호를 리스트에서 제거하고
        tmp //= 2   # 임시값을 2로 나누어준다(이 뒤로는 2배가 적용이 안되기 떄문)

    else:   # 3배를 닫는 괄호의 경우
        if not stack or stack[-1] == "(":   # 2배와 같다
            answer = 0
            break
        if txts[i-1] == "[":
            answer += tmp
        stack.pop()
        tmp //= 3

if stack:   # 스택이 남아있으면
    print(0)   # 0을 출력한다
else:   # 아닌경우
    print(answer)   # 정답을 출력한다(괄호에 오류가 있는 경우 정답을 0처리 해서 가능)


# txts = input()
# L = len(txts)
# for txt in txts:
#     print(txt)
#
# b = [0]
# answer = [0]
# tmp = [0]
# i = [0]
#
#
# def dfs():
#     nonlocal tmp, i
#     i += 1
#     if txts[i] == '(':
#         b.append(2)
#         dfs()
#     if txts[i] == '[':
#         b.append(3)
#         dfs()
#     if txts[i] == ')' and b[-1] == 2:
#         if tmp[-1] == 0:
#             tmp = 2
#         else:
#             tmp[-1] *= 2
#     if txts[i] == ']' and b[-1] == 3:
#         if tmp[-1] == 0:
#             tmp[-1] = 3
#         else:
#             tmp[-1] *= 3
#     if i == L:
#         return True
#
#
# is_done = dfs()
# if is_done:
#     print(answer)
# else:
#     print(0)
