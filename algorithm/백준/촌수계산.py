import sys

input = sys.stdin.readline
T = int(input())
matrix = [0] * (T+1)   # 부모를 저장할 리스트를 0으로 초기화(인덱스를 위해 1개 더 만든다)
s, e = map(int, input().split())   # 촌수 계산을 시작할 번호와 끝낼 번호
N = int(input())
# 부모 정보를 리스트에 저장
for _ in range(N):
    nums = list(map(int, input().split()))
    matrix[nums[1]] = nums[0]

chk = [s]   # 시작부터 윗 세대의 정보를 담을 리스트에 시작 번호를 넣어준다
while True:
    if matrix[s] == 0:   # 부모가 없으면(최상위 노드이면)
        break
    chk.append(matrix[s])   # 세대 정보 리스트에 본인의 부모를 추가하고
    s = matrix[s]   # 시작 번호를 부모로 변경한다

cnt = 0   # 끝낼 번호부터 윗세대로 올라간 횟수를 0으로 초기화한다
while True:
    if e in chk:   # 끝낼 번호가 세대정보 리스트에 있으면(친척이 되는 공통부모)
        print(cnt + chk.index(e))   # 공통 부모의 인덱스(올라간 횟수와 동일)와 올라간 횟수를 더해서 출력한다
        break
    if matrix[e] == 0:   # 더이상 부모가 없는 경우
        print(-1)   # 친척이 아니다
        break
    e = matrix[e]   # 끝낼 번호를 부모의 번호로 변경하고
    cnt += 1   # 올라간 횟수를 1회 추가한다
