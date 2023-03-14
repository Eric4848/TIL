def solution(n, stations, w):
    answer = 0
    stations.append(n)

    for i in range(len(stations)):

        if i == 0:
            connect = stations[0] - w - 1
        else:
            connect = stations[i] - stations[i-1] - 2 * w - 1

        if connect > 0:
            answer += 1
            answer += connect // (2 * w + 1)
            if connect % (2 * w + 1) == 0:
                answer -= 1

    return answer


print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))


# def solution(n, stations, w):
#     answer = 0
#     is_connect = [False] * (n + 2)
#     is_connect[0] = True
#     is_connect[n + 1] = True
#     count = 0
#
#     for ant in stations:
#         for i in range(w + 1):
#             if ant + i <= n:
#                 is_connect[ant + i] = True
#             if ant - i >= 1:
#                 is_connect[ant - i] = True
#
#     for connect in is_connect:
#         if not connect:
#             count += 1
#         if connect:
#             if count != 0:
#                 answer += 1
#                 answer += count // (2 * w + 1)
#                 if count % (2 * w + 1) == 0:
#                     answer -= 1
#             count = 0
#
#     return answer
