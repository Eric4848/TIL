N = int(input())
min_ans = []
max_ans = []
conditions = input().split()

# 최대 숫자열
maximum = 9   # 사용 가능한 최대 숫자를 9로 설정
rev = 0   # 숫자의 정렬 순서가 바뀐 회수를 0으로 초기화
for i in range(N):   # 부등호 갯수만큼
    if conditions[i] == ">":   # 내림차순이면
        if rev:   # 앞서 뒤집힌 적이 있다면
            for j in range(rev + 1):   # 뒤집힌 횟수 + 1만큼 (현재 자리까지 계산하기 위해 1개 더 계산)
                max_ans.append(maximum - rev + j)   # 정답에 역순으로 숫자 저장 (최대숫자 - 뒤집힌 갯수 + 뒤집혀진 번째수 - 1)
            maximum -= rev + 1   # 사용 가능한 최대 숫자를 뒤집힌 갯수 + 1(현재 숫자)만큼 줄인다
            rev = 0   # 뒤집힌 숫자를 0으로 초기화한다
        else:   # 뒤집힌 적이 없다면
            max_ans.append(maximum)   # 최대 숫자를 저장하고
            maximum -= 1   # 1 줄여준다
    else:   # 오름차순이면
        rev += 1   # 뒤집힌 갯수를 1 늘려준다
        if i == N-1:   # 현재 마지막 위치라면
            for j in range(rev):   # 뒤집힌 갯수만큼(위의 경우는 내림차순 계산 / 이곳은 계산 X)
                max_ans.append(maximum - rev + j)   # 역순으로 숫자 저장

max_ans.append(maximum)   # 정답에 최댓값 저장


# 최소 숫자열 - 최대와 반대
minimum = 0
rev = 0
for i in range(N):
    if conditions[i] == "<":
        if rev:
            for j in range(rev + 1):
                min_ans.append(minimum + rev - j)
            minimum += rev + 1
            rev = 0
        else:
            min_ans.append(minimum)
            minimum += 1
    else:
        rev += 1
        if i == N-1:
            for j in range(rev):
                min_ans.append(minimum + rev - j)

min_ans.append(minimum)

print(''.join(map(str, max_ans)))
print(''.join(map(str, min_ans)))
