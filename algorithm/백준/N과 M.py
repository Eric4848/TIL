num, length = map(int, input().split())

answers = []
temp = []


def dfs(prev):
    if len(temp) == length:
        answers.append(temp[:])
        return

    for i in range(1, num + 1):
        if prev > i:
            continue
        temp.append(i)
        dfs(i)
        temp.pop()


dfs(0)
for answer in answers:
    for num in answer:
        print(num, end=' ')
    print('')
