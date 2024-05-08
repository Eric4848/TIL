T = int(input())
for _ in range(T):
    keys = input().rstrip()   # 입력받은 키들
    answer = []   # 정답을 저장할 리스트
    stack = []   # 중간 스택을 저장할 리스트
    for key in keys:   # 각 입력값별로
        if key == '<':   # 좌측이동이면
            if answer:   # 정답에 입력값이 있으면
                stack.append(answer.pop())   # 하나 pop하여 스택에 추가(오른쪽 문자 하나를 빼 왼쪽으로 이동 효과)
        elif key == '>':   # 우측이동이면
            if stack:   # 스택에 입력값이 있으면
                answer.append(stack.pop())   # 하나 pop하여 정답에 추가(우측 문자 하나를 더해 오른쪽으로 이동 효과)
        elif key == '-':   # 제거라면
            if answer:   # 정답에 입력값이 있으면(커서 기준 좌측에 지울 문자가 있으면)
                answer.pop()   # 제거한다
        else:   # 그 외(문자)인 경우
            answer.append(key)   # 정답에 해당 입력 추가

    while stack:   # 스택에 쌓인 문자들을
        answer.append(stack.pop())   # pop하여 정답에 추가

    print(''.join(answer))
