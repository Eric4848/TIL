def solution(sizes):
    row = []
    col = []
    for a, b in sizes:
        if a > b:
            row.append(int(a))
            col.append(int(b))
        else:
            row.append(int(b))
            col.append(int(a))
    answer = max(row) * max(col)
    return answer


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
