N = int(input())
answers = [0, 0, 3]   # N이 0, 1, 2인 경우
for i in range(3, 31):   # 3부터 30까지
    if i % 2 == 0:   # N이 짝수라면
        answers.append(3 * answers[i-2])   # N-2번째 * 3(맨 마지막 두줄에 3가지 모양으로 추가 가능
        for j in range(i-4, -1, -2):   # N-4번째부터 0번째까지
            answers[i] += 2 * answers[j]   # j번째 이후에 맨위나 맨 아래를 한줄로 잇고 좌,우에 세로를 세운 뒤 나머지는 가로로 채우는 경우 2개를 추가 가능
        answers[i] += 2   # 전체에서 맨 위나 맨 아래를 한줄로 잇고 좌, 우에 세로를 세운 뒤 나머지는 가로로 채우는 경우
    else:
        answers.append(0)   # 홀수인 경우 0을 입력
print(answers[N])   # 정답 출력
