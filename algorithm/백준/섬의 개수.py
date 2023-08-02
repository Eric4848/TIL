import sys

sys.setrecursionlimit(10**8)   # 재귀의 깊이 제한을 설정해준다
input = sys.stdin.readline
a, b = map(int, input().split())
dr = [0, 0, 1, -1, 1, 1, -1, -1]   # 열의 위치별 증감을 저장해 둔 리스트
dc = [1, -1, 0, 0, 1, -1, 1, -1]   # 행의 위치별 증감을 저장해 둔 리스트


def search(r, c):   # 섬의 일부가 발견되면 나머지를 찾아주는 함수
    for k in range(8):   # 섬의 일부로부터 8방향으로
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < b and 0 <= nc < a:   # 그 방향이 범위 내에 있고
            if matrix[nr][nc] == 1:   # 섬이라면
                matrix[nr][nc] = 0   # 찾은 것으로 간주, 섬이 아니다 라고 변경한 후(이 함수에 들어온 후에는 0이어도 상관없기 때문에)
                search(nr, nc)   # 그 지점에서 다시 8방향을 찾아준다


while a != 0:   # 입력이 무조건 양의 정수이므로 a나 b가 양수면 계속된다
    answer = 0   # 답을 0개로 초기화 한다
    matrix = [list(map(int, input().split())) for _ in range(b)]
    for i in range(b):   # 열과
        for j in range(a):   # 행을 돌아가며
            if matrix[i][j] == 1:   # 그 위치가 섬인경우
                matrix[i][j] = 0   # 섬이 아니라고 변경한 후
                search(i, j)   # 섬탐색을 진행한다
                answer += 1   # 답을 1개 추가해 준다
    print(answer)
    a, b = map(int, input().split())   # 다음 숫자 두 개를 입력받는다
