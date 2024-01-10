# 별들을 그리는 함수
def drawStar(n):
    if n == 3:   # 가장 최소단위
        return['  *  ', ' * * ', '*****']   # 기본무늬를 반환한다

    stars = []   # 출력할 별들을 담을 리스트
    small = drawStar(n // 2)   # 한 단위 작은 별들을 small에 저장

    for star in small:   # 별의 윗칸은
        stars.append(' ' * (n // 2) + star + ' ' * (n // 2))   # 현재 단위의 반만큼 띄우고 한 단위 작은 별을 출력하고 같은 거리만큼 띄운다

    for star in small:   # 별의 아랫칸은
        stars.append(star + ' ' + star)   # 한 단위 작은 별을 출력하고 한칸 띄운 후 다시 출력한다

    return stars   # 리스트에 담은 별을 반환한다


N = int(input())
print('\n'.join(drawStar(N)))   # 리스트로 받은 별들을 한 줄 씩 출력한다
