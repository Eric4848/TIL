N = int(input())
stack = []
answer = []
now = 1

for i in range(N):
    num = int(input())
    while now <= num:
        answer.append('+')
        stack.append(now)
        now += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        break

    if i == N-1:
        for j in answer:
            print(j)
