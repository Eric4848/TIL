while True:
    n = int(input())
    if n == 0:
        break
    answer = 0
    for i in range(n+1, 2*n + 1):
        answer += 1
        if i == 1:
            answer -= 1
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                answer -= 1
                break
    print(answer)
