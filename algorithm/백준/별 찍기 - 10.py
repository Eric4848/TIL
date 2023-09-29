def star(n):   # 별을 구하는 함수
    if n == 3:   # 가로 개수가 3개가 되면
        return['***', '* *', '***']   # 3X3에서 가운데 빼고 별을 찍은 것을 반환한다

    small = star(n // 3)   # 가로를 3으로 나눈 값에 대해 별을 구한 것을 저장한다
    stars = []   # 찍을 별들을 저장할 리스트를 초기화 한다
    for i in small:   # 맨 윗줄의 경우
        stars.append(i*3)   # 저장 리스트에 작은 것을 3번 곱하여 하여 저장한다

    for i in small:   # 가운데 줄의 경우
        stars.append(i + ' '*(n // 3) + i)   # 저장 리스트에 작은 것을 1번, 작은것의 길이만큼 공백, 다시 작은 것을 1번 저장한다

    for i in small:   # 맨 밑줄의 경우
        stars.append(i*3)   # 맨 윗줄과 같다

    return stars   # 저장한 별들을 반환한다


N = int(input())
print('\n'.join(star(N)))   # 별을 구해서 '\n'과 join하여 한줄씩 출력한다
