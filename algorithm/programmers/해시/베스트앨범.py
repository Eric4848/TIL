def solution(genres, plays):
    answer = []
    counts = {}
    songs = {}
    for i in range(len(genres)):
        if genres[i] in counts:
            counts[genres[i]] += plays[i]
            songs[genres[i]].append((i, plays[i]))
        else:
            counts[genres[i]] = plays[i]
            songs[genres[i]] = [(i, plays[i])]
    rank = sorted(counts, key=lambda x: counts[x], reverse=True)
    for genres in rank:
        temp = sorted(songs[genres], key=lambda x: (x[1], -x[0]), reverse=True)
        print(temp)
        added = 0
        for song in temp:
            answer.append(song[0])
            added += 1
            if added == 2:
                break
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [800, 600, 150, 800, 2500]))

# def solution(genres, plays):
#     answer = []
#     d = {} # hash
#     dN = {} # for calculating genres rank
#
#     # assigning into dictionary
#     for i in range(len(genres)):
#         if genres[i] in d:
#             d[genres[i]].append((plays[i], i))
#             dN[genres[i]] += plays[i]
#         else:
#             d[genres[i]] = [(plays[i], i)]
#             dN[genres[i]] = plays[i]
#
#     # sorting in descending order for genres rank popularity.
#     rank = sorted(dN, key=lambda x:dN[x], reverse=True)
#
#     # getting item(genres) in descending order.
#     for item in rank:
#         # sorting songs based on the number of plays in descending order.
#         temp = sorted(d[item], key=lambda x:(x[0],-x[1]), reverse=True)
#         # printing twice only.
#         for i in range(2):
#             answer.append(temp[i][1])
#             # if a particular genre has only one song, break the loop.
#             if len(d[item])<2: break
#     return answer
