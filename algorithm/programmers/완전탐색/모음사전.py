def solution(word):
    answer = 0
    dicts = ['A', 'E', 'I', 'O', 'U']
    counts = [780, 155, 30, 5, 0]
    for i in range(len(word)):
        for j in range(len(dicts)):
            if word[i] == dicts[j]:
                answer += counts[i] * j + j + 1
    return answer


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))


# def solution(word):
#     answer = 0
#     for i, n in enumerate(word):
#         answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
#     return answer
