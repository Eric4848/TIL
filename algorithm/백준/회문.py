T = int(input())
for _ in range(T):
    text = input()
    shift = 0   # 이동한 횟수 초기화
    # 회문 확인
    for i in range(len(text) // 2):   # 길이의 절반만큼(홀수인 경우 가운데는 확인 안해도 된다)
        if text[i] != text[-1-i]:   # 앞뒤의 위치별로 비교하여 서로 다르면
            shift = 1   # 이동횟수를 1 늘리고
            break   # 확인을 중단한다
    # 유사 회문 확인
    if shift:   # 이동해야 한다면
        chk = 0   # 앞, 뒤의 불가능여부를 초기화
        # 앞 이동
        for j in range(i, len(text) // 2):   # 회문이 아닌 곳 부터 길이의 절반만큼(짝수의 경우 가운데로 합쳐져 그대로 해도 된다)
            if text[j+1] != text[-1-j]:   # 앞을 하나 미뤄 회문 비교하여 다르면
                chk += 1   # 불가능을 1 늘린다
                break
        # 뒤 이동
        for j in range(i, len(text) // 2):
            if text[j] != text[-2-j]:   # 뒤를 하나 당겨 회문 비교하여 다르면
                chk += 1   # 불가능을 1 늘린다
                break

        if chk == 2:   # 양측 다 불가능하면
            shift = 2   # 이동 횟수를 2로 바꾼다
    print(shift)   # 이동 횟수(정답)를 출력
