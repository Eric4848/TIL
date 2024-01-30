import sys


# 뒤집는 함수
def switch(R, C):
    for i in range(3):   # 3칸씩
        for j in range(3):
            if mata[R+i][C+j]:   # 해당칸이 1이면
                mata[R+i][C+j] = 0   # 0으로 변환
            else:   # 0이면
                mata[R+i][C+j] = 1   # 1로 변환


# 같은지 확인하는 함수
def chk():
    for r in range(N):   # row
        for c in range(M):   # col 별로
            if mata[r][c] != matb[r][c]:   # 다르면
                print(-1)   # -1 출력
                return   # 종료

    print(answer)   # 전부 같다면 정답 출력
    return


input = sys.stdin.readline
N, M = map(int, input().split())
mata = [list(map(int, input().rstrip())) for _ in range(N)]
matb = [list(map(int, input().rstrip())) for _ in range(N)]
answer = 0

for r in range(N-2):   # 길이 -2만큼(3칸씩 같이 뒤집히기때문)
    for c in range(M-2):
        if mata[r][c] != matb[r][c]:   # 다르면
            switch(r, c)   # 뒤집고
            answer += 1   # 정답 + 1

chk()
