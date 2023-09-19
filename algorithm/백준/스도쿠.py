sudoku = [list(map(int, input().split())) for _ in range(9)]
blank = []   # 빈칸들의 위치를 초기화 하고
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append((i, j))   # 빈칸들의 위치를 추가한다


def find(d):   # 빈칸의 숫자를 찾는 함수
    if d == len(blank):   # 찾은 갯수가 빈칸과 같다면
        for i in range(9):
            print(*sudoku[i])   # 스도쿠 판을 출력한 후
        exit(0)   # 함수를 종료한다

    r = blank[d][0]   # 빈칸의 가로 위치
    c = blank[d][1]   # 빈칸의 세로 위치

    for i in range(1, 10):   # 1 ~ 9까지
        if checkRow(r, i) and checkCol(c, i) and checkRec(r, c, i):   # 가로줄, 세로줄, 사각형을 확인해서 넣을 수 있다면
            sudoku[r][c] = i   # 그 숫자를 넣고
            find(d + 1)   # 다음 빈칸을 찾아준다
            sudoku[r][c] = 0   # 다시 숫자를 빼준다


def checkRow(r, n):   # 가로줄 확인
    for i in range(9):
        if sudoku[r][i] == n:   # 가로줄에 넣으려는 수가 있으면
            return False   # False 반환
    return True   # 없으면 True 반환


def checkCol(c, n):   # 세로줄 확인
    for i in range(9):
        if sudoku[i][c] == n:   # 세로줄에 넣으려는 수가 있으면
            return False   # False 반환
    return True   # 없으면 True 반환


def checkRec(r, c, n):   # 사각형 확인
    fr = r // 3 * 3   # 3으로 나눈 몫(항상 양수이므로 나머지 버림)에 3을 곱해 가로 기준선을 만든다
    fc = c // 3 * 3   # 3으로 나눈 몫(항상 양수이므로 나머지 버림)에 3을 곱해 세로 기준선을 만든다
    for i in range(3):
        for j in range(3):
            if sudoku[fr + i][fc + j] == n:   # 각 기준점으로부터 3 X 3 이내에 넣으려는 수가 있으면
                return False   # False 반환
    return True   # 없으면 True 반환


find(0)   # 빈칸 찾는 함수를 실행시킨다
