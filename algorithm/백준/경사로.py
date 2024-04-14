N, L = map(int, input().split())


# 해당 줄이 지나갈 수 있는지 확인하는 함수
def check(hill):
    is_used = [False for _ in range(N)]   # 경사로를 뒀는 지 초기화
    for i in range(N-1):   # 두개를 비교하기때문에 N-1
        if hill[i] != hill[i+1]:   # 다음 칸과 높이가 다르다면
            if abs(hill[i] - hill[i+1]) != 1:   # 높이차가 1이 아닌 경우
                return False   # 불가능
            else:   # 높이차가 1인 경우
                if hill[i] - hill[i+1] == 1:   # 내려가는 경우
                    if N <= i + L:   # 현재높이 + 경사로길이가 N보다 크거나 같다면
                        return False   # 불가능
                    bottom = hill[i+1]   # 경사로를 놓을 바닥의 높이
                    for j in range(i+1, i+L+1):   # 다음칸부터 L개
                        if is_used[j] or hill[j] != bottom:   # 이미 경사로를 뒀거나 칸의 높이가 바닥과 다르면
                            return False   # 불가능
                        is_used[j] = True   # 그 칸에 경사로를 둠 처리
                else:   # 높이차가 -1인 경우
                    if i + 1 - L < 0:   # i+1칸부터 L개 가 0보다 작다면
                        return False   # 불가능
                    bottom = hill[i]   # 경사로를 놓을 바닥의 높이
                    for j in range(i, i-L, -1):   # i부터 L개 뒤로
                        if is_used[j] or hill[j] != bottom:   # 이미 경사로를 뒀거나 칸의 높이가 바닥과다르면
                            return False   # 불가능
                        is_used[j] = True   # 그 칸에 경사로를 둠 처리
    return True   # 모든칸을 지나갈 수 있다


hills = [list(map(int, input().split())) for _ in range(N)]
answer = 0
# 가로 기준
for i in range(N):
    if check(hills[i]):
        answer += 1

# 세로 기준
for j in range(N):
    if check([hills[i][j] for i in range(N)]):
        answer += 1

print(answer)
