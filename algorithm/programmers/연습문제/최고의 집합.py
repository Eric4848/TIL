def solution(n, s):
    answer = []
    col = s // n
    p = s % n
    for _ in range(n):
        answer.append(col)
    for i in range(p):
        answer[n-i-1] += 1
    answer
    if s >= n:
        return answer
    else:
        return [-1]


print(solution(2, 9))
