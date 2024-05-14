import sys

input = sys.stdin.readline
S = input().rstrip()
T = input().rstrip()
chk = 1   # 변경 가능여부 초기화
while S != T:   # 두 문자열이 같아질때까지
    if len(T) == 0:   # 두번쨰 문자열이 다 사라지면
        chk = 0   # 불가능
        break   # 중지
    # 맨 뒤가 A인 경우
    if T[-1] == 'A':
        T = T[:-1]   # 맨 뒤 문자 제거(더하기의 반대)

    # 맨 뒤가 B인 경우
    elif T[-1] == 'B':
        T = T[:-1]   # 맨 뒤 문자 제거
        T = T[::-1]   # 뒤집기
    # 다른 문자인 경우
    else:
        chk = 0   # 불가능
        break   # 중지

if chk:   # 가능하면
    print("1")   # 1
else:   # 불가능하면
    print('0')   # 0
