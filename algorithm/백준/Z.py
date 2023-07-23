N, r, c = map(int, input().split())
answer = 0
while N != 0:
    N -= 1
    x = 2 ** N
    if r < x and c < x:
        continue
    elif r < x and x <= c:
        answer += x * x
    elif x <= r and c < x:
        answer += x * x * 2
    else:
        answer += x * x * 3

print(answer)
