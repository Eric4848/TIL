T = int(input())
for _ in range(T):
    genes = input().rstrip()
    # 시작 가능 문자
    if genes[0] in ['B', 'C', 'D', 'E', 'F']:   # 'A'를 제외한 시작 문자가 있다면
        genes = genes[1:]   # 하나 제거
    # 종료 가능 문자
    if genes[-1] in ['A', 'B', 'D', 'E', 'F']:   # 'C'를 제외한 종료 가능 문자가 있다면
        genes = genes[:-1]   # 하나 제거
    # 첫 번째 조건
    while genes and genes[0] == 'A':   # 'A'가 처음 위치에 있다면
        genes = genes[1:]   # 제거
    # 두 번쨰 조건
    while genes and genes[0] == 'F':   # 'F'가 처음 위치에 있다면
        genes = genes[1:]   # 제거
    # 세 번째 조건
    while genes and genes[0] == 'C':   # 'C'가 처음 위치에 있다면
        genes = genes[1:]   # 제거

    # 판단
    if genes:   # 염색체가 남아있다면
        print('Good')   # 'Good' 출력
    else:   # 남아있지 않다면(조건에 맞다면)
        print('Infected!')   # 'Infected!' 출력
