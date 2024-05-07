S = input().rstrip()
chk = False   # 태그인지를 초기화
answer = []   # 정답을 담을 리스트
stack = []   # 역순을 담을 리스트
for s in S:   # 문자별로
    if s == '>':   # 태그의 끝인경우
        answer.append(s)   # 문자를 입력하고
        chk = False   # 태그가 아니다로 변경

    elif chk:   # 태그인 경우
        answer.append(s)   # 문자를 정답에 바로 추가

    elif s == ' ':   # 공백인 경우
        while stack:   # 스택에 쌓인 문자만큼
            answer.append(stack.pop())   # pop하여 정답에 추가
        answer.append(s)   # 정답에 공백 추가

    elif s == '<':   # 태그의 시작인 경우
        while stack:   # 스택에 쌓인 문자만큼
            answer.append(stack.pop())   # pop하여 정답에 추가
        answer.append(s)   # 문자를 입력하고
        chk = True   # 태그이다로 변경

    else:   # 일반 문자인 경우
        stack.append(s)   # 스택에 추가

while stack:   # 스택에 쌓인 문자만큼
    answer.append(stack.pop())   # pop하여 정답에 추가

print(''.join(answer))
