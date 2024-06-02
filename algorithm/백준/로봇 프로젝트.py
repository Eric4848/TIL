import sys

input = sys.stdin.readline
while True:
    # 케이스 확인
    try:
        W = int(input()) * 10 ** 7   # 입력받기 시도
    except:   # 없다면
        break   # 종료

    legos = []   # 레고들의 크기를 담을 리스트
    n = int(input())
    # 레고 크기 저장
    for _ in range(n):
        legos.append(int(input()))
    legos.sort()   # 레고 정렬

    chk = 1   # 불가능하다 표시
    l = 0   # 작은 레고 위치
    r = n-1   # 큰 레고 위치
    # 두 포인터
    while l < r:
        t = legos[l] + legos[r]   # 두 레고를 더한 크기
        if t == W:   # 조건과 맞다면
            print('yes', legos[l], legos[r])   # 출력
            chk = 0   # 가능으로 변경
            break   # 종료
        elif t < W:   # 조건보다 작다면
            l += 1   # 작은것을 키운다
        else:   # 조건보다 크다면
            r -= 1   # 큰것을 줄인다
    if chk:   # 불가능한 경우
        print('danger')   # 출력
