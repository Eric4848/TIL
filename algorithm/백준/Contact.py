import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    mw = input().rstrip()   # 전파를 입력받음 / rstrip으로 \n 제거
    answer = 1   # 패턴에 맞다고 초기화
    while mw:   # 전파 조사
        # 두 번째 조건
        if mw[:2] == '01':   # 시작이 '01'인 경우
            mw = mw[2:]   # '01' 제거
        # 첫 번쨰 조건
        elif mw[:3] == '100':   # 시작이 '100'인 경우
            mw = mw[3:]   # '100' 제거
            while mw and mw[0] == '0':   # 전파가 남아있고 시작값이 '0'이라면
                mw = mw[1:]   # 제거(100+이므로)
            # 1이 없는 경우
            if not mw:   # 전파가 남아있지 않은경우(1이 없는경우 -> 0은 모두 제거했으므로)
                answer = 0   # 패턴에 맞지 않다고 변경
                break   # 종료
            # '1' 1개 제거
            mw = mw[1:]   # 반드시 1이므로 확인하지 않아도 된다
            # 이어지는 1 판단
            while mw and mw[0] == '1':   # 전파가 남아있고 그 시작값이 '1'인 경우
                if 3 <= len(mw) and mw[1:3] == '00':   # 전파 길이가 3 이상이고 두,세번째가 '00'이라면
                    break   # 종료(첫 번째 조건에 맞으므로 계산을 위해)
                else:   # 첫 번째 조건에 맞지 않다면
                    mw = mw[1:]   # '1' 제거
        else:   # 두 조건에 맞지 않다면
            answer = 0   # 패턴에 맞지 않다고 변경
            break   # 종료

    if answer:   # 패턴에 맞으면
        print('YES')   # YES
    else:   # 맞지 않으면
        print('NO')   # NO
