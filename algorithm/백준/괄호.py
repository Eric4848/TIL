import sys


# 입력을 확인하는 함수
def check():
    stack = 0   # 여는 괄호 갯수 0개로 초기화
    for ps in st:
        if ps == '(':   # 여는 괄호인 경우
            stack += 1   # 스택 1 추가
        else:   # 닫는 괄호인 경우
            if stack:   # 스택이 있다면
                stack -= 1   # 1개 빼준다
            else:   # 스택이 없다면
                return 'NO'   # 아니다
    # 결과
    if not stack:   # 스택이 0이면
        return 'YES'   # 맞다
    else:   # 0이 아니면
        return 'NO'   # 아니다


input = sys.stdin.readline
N = int(input())
for _ in range(N):
    st = input().rstrip()
    print(check())   # 확인 결과 출력
