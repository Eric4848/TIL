def solution(numbers):
    answer = ''
    temp = []
    for number in numbers:
        temp.append((str(number)*4, len(str(number))))
    temp.sort(reverse=True)
    print(temp)
    for number, length in temp:
        if answer == '0' and number[:length] == 0:
            continue
        answer += number[:length]
    return answer


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
