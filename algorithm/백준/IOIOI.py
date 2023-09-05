N = int(input())
M = int(input())
S = input()
answer = 0
idx = 0   # 문자열의 인덱스
cnt = 0   # IOI의 반복 횟수 저장

while idx < (M-2):   # 마지막에서 세번째 까지
    if S[idx:idx+3] == 'IOI':   # IOI의 문자열이면
        cnt += 1   # 반복횟수를 1 늘려주고
        idx += 2   # 인덱스를 2개 늘려 뒤쪽 I로 맞춰준다
        if cnt == N:   # 반복 횟수가 조건의 횟수와 같다면
            answer += 1   # 정답을 1늘려주고
            cnt -= 1   # 반복횟수를 1 줄여준다
    else:   # 문자열이 IOI가 아니면
        idx += 1   # 다음 문자로 넘기고
        cnt = 0   # 반복횟수를 초기화한다

print(answer)
