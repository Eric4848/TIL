texts = list(input())
N = int(input())
length = len(texts)
position = length

for _ in range(N):
    a = list(input().split())
    if a[0] == 'L':
        if 0 < position:
            position -= 1
    if a[0] == 'D':
        if position < length:
            position += 1
    if a[0] == 'B':
        if 0 < position:
            texts = texts[0:position-1] + texts[position:]
            position -= 1
    if a[0] == 'P':
        texts = texts[0:position] + [a[1]] + texts[position:]
        position += 1

print(''.join(texts))
