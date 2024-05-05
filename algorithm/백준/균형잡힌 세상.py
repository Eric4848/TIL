import sys

input = sys.stdin.readline
while True:
    texts = input().rstrip()
    if texts == '.':   # .이 입력되면
        break   # 종료

    stack = []   # 괄호 정보를 담을 스택
    chk = 0   # 불가능 여부 초기화

    for text in texts:   # 각 문자별로
        if text == '(' or text == '[':   # 여는 괄호인 경우
            stack.append(text)   # 스택에 추가

        elif text == ')':   # 닫는 소괄호인 경우
            if stack and stack[-1] == '(':   # 스택이 있고 가장 최근이 여는 소괄호인 경우
                stack.pop()   # 스택에서 pop
            else:   # 아닌경우
                chk = 1   # 불가능
                break   # 문자 탐색 종료

        elif text == ']':   # 닫는 중괄호인 경우
            if stack and stack[-1] == '[':   # 스택이 있고 가장 최근이 여는 중괄호인 경우
                stack.pop()   # 스택에서 pop
            else:   # 아닌경우
                chk = 1   # 불가능
                break   # 문자 탐색 종료

    if stack or chk:   # 스택에 남아있는 것이 있거나 불가능 처리라면
        print('no')   # no 출력
    else:   # 가능한 경우
        print('yes')   # yes 출력
