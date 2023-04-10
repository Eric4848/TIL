num = int(input())
answers = []
temp = []
is_used = [False for _ in range(num + 1)]


def dfs():
    if len(temp) == num:
        answers.append(temp[:])
        return
    for n in range(1, num + 1):
        if not is_used[n]:
            temp.append(n)
            is_used[n] = True
            dfs()
            temp.pop()
            is_used[n] = False


dfs()
for answer in answers:
    print(*answer)
