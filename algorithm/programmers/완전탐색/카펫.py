def solution(brown, yellow):
    answer = []
    y = int(brown/2)
    x = 2
    while y > 1:
        if (y-2) * (x-2) == yellow:
            answer.append(y)
            answer.append(x)
            break
        y -= 1
        x += 1
    return answer


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
