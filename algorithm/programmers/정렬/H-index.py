def solution(citations):
    answer = len(citations)
    citations.sort()

    for i in range(answer):
        if citations[i] >= answer - i:
            break
    if citations[answer - 1] == 0:
        i = answer
    return answer - i


print(solution([100, 100, 100]))
