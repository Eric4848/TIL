# 변환시키는 함수(목표를 원본으로 변경)
def dfs(st):
    # 강제 종료
    if not st:   # 변경시키 문자가 없다면
        return   # 종료
    # 변경 가능
    if st == S:   # 원본과 동일하다면
        print(1)   # 가능 출력
        exit()   # 정지
    # 첫 번째 방법
    if st[-1] == 'A':   # 맨 뒤 문자가 'A'라면
        dfs(st[:-1])   # 'A'를 제거하여 다음 변환
    # 두 번째 방법
    if st[0] == 'B':   # 맨 앞 문자가 'B'라면
        tmp = st[1:]   # 맨앞 문자를 제거
        tmp = tmp[::-1]   # 순서를 뒤집어
        dfs(tmp)   # 다음 변환


S = input().rstrip()
T = input().rstrip()
dfs(T)   # 목표 문자를 변환
print(0)   # 변환함수를 거쳐도 불가능하면 불가능 출력
