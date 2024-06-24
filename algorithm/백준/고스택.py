import sys

input = sys.stdin.readline
maximum = 10 ** 9   # 최대치 조건


# 계산하는 함수
def calc(num):   # 스택의 시작 숫자를 받는다
    stack = [num]   # 입력받은 숫자를 스택에 추가
    for order in orders:   # 명령의 순서대로
        # NUM
        if order[:3] == 'NUM':   # 길이가 3보다 크면(추가명령인 경우)
            tmp = int(order[4:])   # 숫자부분을 int로 형변환
            stack.append(tmp)   # 스택에 추가

        # 이후 명령은 스택에 1개 이상 필요 -> 스택이 없으면 에러
        elif not stack:
            return 'ERROR'

        # POP
        elif order == 'pop':
            stack.pop()

        # INV
        elif order == 'INV':
            stack[-1] *= -1   # 마지막 숫자에 -1을 곱해준다

        # DUP
        elif order == 'DUP':
            stack.append(stack[-1])   # 마지막 숫자를 스택에 추가한다

        # 이후 명령은 스택에 2개 이상 필요 -> 스택이 2 미만이면 에러
        elif len(stack) < 2:
            return 'ERROR'

        # SWP
        elif order == 'SWP':
            a = stack.pop()   # 첫번째 숫자 pop
            b = stack.pop()   # 두번쨰 슷지 pop
            stack.append(a)   # 첫번째 먼저 추가
            stack.append(b)   # 두번쨰 추가

        # ADD
        elif order == 'ADD':
            tmp = stack.pop() + stack.pop()   # 앞쪽 두 숫자를 pop하여 더한다
            if maximum < abs(tmp):   # 결과의 절댓값이 제한보다 크다면
                return 'ERROR'   # 에러
            stack.append(tmp)   # 스택에 값 추가

        # SUB
        elif order == 'SUB':
            tmp = -stack.pop() + stack.pop()   # 앞 숫자를 pop해 -, 뒷수자를 pop해 더해준다
            if maximum < abs(tmp):   # 결과의 절댓값이 제한보다 크다면
                return 'ERROR'   # 에러
            stack.append(tmp)   # 스택에 값 추가

        # MUL
        elif order == 'MUL':
            tmp = stack.pop() * stack.pop()   # 앞쪽 두 숫자를 pop하여 곱한다
            if maximum < abs(tmp):   # 결과의 절댓값이 제한보다 크다면
                return 'ERROR'   # 에러
            stack.append(tmp)   # 스택에 값 추가

        # DIV
        elif order == 'DIV':
            a = stack.pop()   # 첫번째 숫자
            b = stack.pop()   # 두번째 숫자
            if a == 0:   # 첫번째 숫자가 0이면
                return 'ERROR'   # 에러

            # 계산
            tmp = abs(b) // abs(a)   # 두번째 숫자의 절댓값을 첫번째 숫자의 절댓값으로 나눈 몫
            if maximum < abs(tmp):   # 결과의 절댓값이 제한보다 크다면
                return 'ERROR'   # 에러

            # 부호
            if a < 0 < b or b < 0 < a:   # 두 숫자의 부호가 다르다면
                tmp = -tmp   # -로 변경
            stack.append(tmp)   # 스택에 추가

        # MOD
        elif order == 'MOD':
            a = stack.pop()   # 첫번째 숫자
            b = stack.pop()   # 두번째 숫자
            if a == 0:   # 첫번째 숫자가 0이면
                return 'ERROR'   # 에러

            # 계산
            tmp = abs(b) % abs(a)   # 두번째 숫자의 절댓값을 첫번째 숫자의 절댓값으로 나눈 나머지
            if maximum < abs(tmp):   # 결과의 절댓값이 제한보다 크다면
                return 'ERROR'   # 에러

            # 부호
            if b < 0:   # 두번째 숫자가 음수라면
                tmp = -tmp   # -로 변경
            stack.append(tmp)   # 스택에 추가

        # 이상값
        else:
            return 'ERROR'   # 에러

    if len(stack) == 1:   # 스택에 1개만 있다면
        return stack[0]   # 반환
    return 'ERROR'   # 에러


while True:
    orders = []

    while True:
        odr = input().strip()   # 명령 입력받음
        if odr == 'QUIT':   # 종료명령인 경우
            quit()   # 종료
        if odr == 'END':   # 끝인 경우
            break   # 입력 중단
        orders.append(odr)   # 명령 입력

    n = int(input())   # 숫자의 갯수
    for _ in range(n):   # 숫자별로
        print(calc(int(input())))   # 계산 진행

    print()   # 1줄 띄우기
    input()   # 빈줄 입력 넘기기
