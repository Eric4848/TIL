first = input()
second = input()
answers = [[] for _ in range(len(first))]   # 겹치는 알파벳들을 저장할 리스트

for i in range(len(second)):   # 두번째 알파벳들에 대해
    word = []   # 현재까지 겹친 단어를 빈 리스트로 초기화
    for j in range(len(first)):   # 첫번째 알파벳들에 대해
        if len(word) < len(answers[j]):   # 현재 겹친 것 보다 해당 위치의 겹친 알파벳들이 더 많다면
            word = answers[j]   # 저장된 알파벳들을 불러오고
        elif first[j] == second[i]:   # 길이기 갈진 않고 두 위치의 알파벳들이 같다면
            answers[j] = word + [first[j]]   # 여태까지 겹친 알파벳에 현재 알파벳을 더해 저장한다

maximum = 0   # 가장 길게 겹친 부분을 0으로 초기화
answer = 0   # 정답이 저장된 위치를 0으로 초기화
for i in range(len(answers)):   # 정답 중
    if maximum < len(answers[i]):   # 가장 길게 겹친 부분보다 길다면
        answer = i   # 그 정답의 위치를 저장하고
        maximum = len(answers[i])   # 길이를 변경한다

print(len(answers[answer]))   # 정답의 길이를 출력한다
if len(answers[answer]):   # 겹치는 문자가 있다면
    print(''.join(answers[answer]))   # 문자들을 출력한다
