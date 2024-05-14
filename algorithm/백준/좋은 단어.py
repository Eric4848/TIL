N = int(input())
answer = 0
for _ in range(N):
    words = input().rstrip()
    stack = []   # 스택을 담을 리스트
    for word in words:   # 단어의 문자별로
        if stack and stack[-1] == word:   # 스택에 문자가 있고, 마지막 문자가 해당 문자와 같다면
            stack.pop()   # 스택에서 제거(이어준다)
        else:   # 스택이 비었거나 입력과 마지막이 다르면
            stack.append(word)   # 해당 문자를 스택에 추가

    if not stack:   # 스택에 남은 문자가 없다면
        answer += 1   # 정답에 1추가
print(answer)
