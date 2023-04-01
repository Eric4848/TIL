def solution(s):
    a = list(s)
    b = s.lower()
    c = list(b)
    c[0] = a[0].upper()
    for i in range(len(s) - 1):
        if a[i] == ' ':
            c[i + 1] = a[i + 1].upper()
    answer = ''.join(c)
    return answer


print(solution("3people unFollowed me"))
