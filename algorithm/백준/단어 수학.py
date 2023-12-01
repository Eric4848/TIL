N = int(input())
alphs = {}   # 알파벳들을 담을 딕셔너리
answer = 0   # 정답을 0으로 초기화
for _ in range(N):
    word = input()
    L = len(word)
    for i in range(L):
        weight = 1 * 10 ** (L-i-1)   # 숫자의 자리만큼 계산
        if word[i] in alphs:   # 딕셔너리에 해당 알파벳이 있으면
            alphs[word[i]] += weight   # 값에 자릿값을 더한다
        else:   # 없으면
            alphs[word[i]] = weight   # 새로 추가한다

weight = 9   # 가능한 가장 큰 수인 9부터
for value in sorted(alphs, key=lambda x: alphs[x], reverse=True):   # 알파벳의 자릿값이 큰순서대로
    answer += weight * alphs[value]   # 정답에 가중치와 자릿값을 곱해서 더한다
    weight -= 1   # 가중치를 1 줄인다
print(answer)
