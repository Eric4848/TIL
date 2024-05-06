bars = input().rstrip()
answer = 0
cnt = 0   # 막대기의 갯수

for i in range(len(bars)):
    # 여는 괄호인 경우
    if bars[i] == '(':
        cnt += 1   # 막대기 갯수 + 1
    # 닫는 괄호인 경우
    else:
        if bars[i-1] == '(':   # 레이저라면
            cnt -= 1   # 막대기 갯수 - 1 (레이저이므로)
            answer += cnt   # 정답에 막대 갯수 더하기(자른 막대 갯수)
        else:   # 막대의 끝이라면
            answer += 1   # 정답에 1개 추가
            cnt -= 1   # 막대기 갯수 - 1

print(answer)
