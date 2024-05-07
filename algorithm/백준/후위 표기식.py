calcs = input().rstrip()
priority = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
stack = []   # 연산자들을 담을 리스트
answer = []   # 변환한 정답을 담을 리스트

for calc in calcs:   # 입력 문자마다
    if calc.isalpha():   # 알파벳인 경우
        answer.append(calc)   # 정답에 저장
    # 연산자들 중
    elif not stack:   # 스택이 없는 경우
        stack.append(calc)   # 스택에 추가

    elif calc == '(':   # 여는 괄호인 경우
        stack.append(calc)   # 스택에 추가

    elif calc == ')':   # 닫는 괄호인 경우
        while stack[-1] != '(':   # 괄호 시작이 될 때 까지
            answer.append(stack.pop())   # 스택의 연산자들을 pop하여 정답에 추가
        stack.pop()   # 여는 괄호를 스택에서 제거

    else:   # 스택이 있는 경우
        while stack and priority[calc] <= priority[stack[-1]]:   # 스택이 있고 현재 우선 순위가 스택 마지막보다 작거나 같다면
            answer.append(stack.pop())   # 해당 연산자를 pop하여 정답에 추가
        stack.append(calc)   # 스택에 현재 연산자 추가

while stack:   # 스택에 연산자가 남아있으면
    answer.append(stack.pop())   # pop하여 정답에 추가

print(''.join(answer))
