def solution(answers):
    answer = []
    total = 0
    for n in range(len(answers)):
        if answers[n] == n % 5 + 1:
            total += 1
        if n == (len(answers) - 1):
            answer.append(total)

    total = 0
    for n in range(len(answers)):
        if n % 2 == 0:
            if answers[n] == 2:
                total += 1
        else:
            if (n // 2) % 4 == 0:
                if answers[n] == 1:
                    total += 1
            elif (n // 2) % 4 == 1:
                if answers[n] == 3:
                    total += 1
            elif (n // 2) % 4 == 2:
                if answers[n] == 4:
                    total += 1
            elif (n // 2) % 4 == 3:
                if answers[n] == 5:
                    total += 1
        if n == (len(answers) - 1):
            answer.append(total)

    total = 0
    for n in range(len(answers)):
        if n % 10 == 0 or n % 10 == 1:
            if answers[n] == 3:
                total += 1
        if n % 10 == 2 or n % 10 == 3:
            if answers[n] == 1:
                total += 1
        if n % 10 == 4 or n % 10 == 5:
            if answers[n] == 2:
                total += 1
        if n % 10 == 6 or n % 10 == 7:
            if answers[n] == 4:
                total += 1
        if n % 10 == 8 or n % 10 == 9:
            if answers[n] == 5:
                total += 1

        if n == (len(answers) - 1):
            answer.append(total)
    winner = []
    problem = len(answers)

    while not winner:
        for n in range(len(answer)):
            if answer[n] == problem:
                winner.append(n+1)
        problem -= 1

    return winner


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))

# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []
#
#     for idx, answer in enumerate(answers):
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1
#
#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)
#
#     return result
