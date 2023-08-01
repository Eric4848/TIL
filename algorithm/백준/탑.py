N = int(input())
towers = list(map(int, input().split()))
answers = [0] * N
stack = []
for i in range(N):
    while stack:   # 스택에 저장된 탑마다
        if stack[-1][1] < towers[i]:   # 마지막 저장된 탑의 크기보다 현재 탑이 더 큰 탑이면
            stack.pop()   # 그 탑을 제거해 준다
        else:
            answers[i] = stack[-1][0]+1   # 마지막 저장된 탑의 위치를 정답에 넣어준다
            break
    stack.append((i, towers[i]))   # 스택에 탑 위치와 높이를 저장한다
print(*answers)
