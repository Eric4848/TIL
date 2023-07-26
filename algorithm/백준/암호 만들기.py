from itertools import combinations   # 순서가 고정되어 있으므로 순열을 사용한다
L, C = map(int, input().split())
alphs = sorted(list(map(str, input().split())))   # 암호로 쓰일 알파벳들을 순서를 맞춰 저장한다
for comb in combinations(alphs, L):   # 알파벳들 중
    a = 0   # 모음의 숫자를 초기화한다
    answer = []   # 정답 암호를 저장할 리스트를 초기화한다
    # for i in range(L):   # 순열의 번호로 계산한 부분(바로 계산할 수 있기때문에 수정)
    #     #     answer += comb[i]
    #     #     if comb[i] == 'a' or comb[i] == 'e' or comb[i] == 'i' or comb[i] == 'o' or comb[i] == 'u':
    for alph in comb:   # 순열의 각 자리 알파벳 별로
        answer += alph   # 정답 암호에 추가하고
        if alph == 'a' or alph == 'e' or alph == 'i' or alph == 'o' or alph == 'u':   # 모음이면
            a += 1   # 모음 갯수를 1개 늘려준다
    b = L - a   # 자음 갯수는 암호 길이 - 모음 갯수
    if 0 < a and 1 < b:   # 자, 모음이 조건에 맞으면
        print(''.join(answer))   # 답을 출력한다
