import sys

input = sys.stdin.readline
N = int(input())
patterns = input().rstrip()   # 패턴을 rstrip으로 저장 (\n 제거)
# *위치 검색
for i, p in enumerate(patterns):
    if p == '*':   # *위치일 떄
        H = i   # 인덱스(앞쪽 길이)를 H로 저장
        break   # 종료
T = len(patterns) - H - 1   # 뒤쪽 길이를 총 길이 - 앞 길이 - 1로 저장
head = patterns[:H]   # 시작 패턴 저장
tail = patterns[-T:]   # 종료 패턴 저장
# 파일별 검사
for _ in range(N):
    file = input().rstrip()
    if file[:H] == head:   # 시작 부분이 시작 조건에 맞다면
        file = file[H:]   # 시작 조건 부분을 제거하여 저장
        if file[-T:] == tail:   # 종료 부분이 종료 조건에 맞다면
            print('DA')   # 'DA' 출력
        else:   # 종료 조건에 맞지 않다면
            print('NE')   # 'NE' 출력

    else:   # 시작 조건에 맞지 않다면
        print('NE')   # 'NE' 출력


# 오답
# import sys
#
# input = sys.stdin.readline
# N = int(input())
# patterns = input().rstrip()
# for i, p in enumerate(patterns):
#     if p == '*':
#         H = i
#         break
# T = len(patterns) - H - 1
# head = patterns[:H]
# tail = patterns[-T:]
#
# for _ in range(N):
#     file = input().rstrip()
#     if file[:H] == head and file[-T:] == tail:
#         print('DA')
#     else:
#         print('NE')
