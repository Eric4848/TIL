txts = input()
L = len(txts)
for txt in txts:
    print(txt)

b = [0]
answer = [0]
tmp = [0]
i = [0]


def dfs():
    nonlocal tmp, i
    i += 1
    if txts[i] == '(':
        b.append(2)
        dfs()
    if txts[i] == '[':
        b.append(3)
        dfs()
    if txts[i] == ')' and b[-1] == 2:
        if tmp[-1] == 0:
            tmp = 2
        else:
            tmp[-1] *= 2
    if txts[i] == ']' and b[-1] == 3:
        if tmp[-1] == 0:
            tmp[-1] = 3
        else:
            tmp[-1] *= 3
    if i == L:
        return True


is_done = dfs()
if is_done:
    print(answer)
else:
    print(0)
