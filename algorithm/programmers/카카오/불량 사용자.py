from itertools import permutations


def solution(user_id, banned_id):
    answer = 0
    ban = len(banned_id)
    bans = {}
    temp = []
    for banned in banned_id:
        for user in user_id:
            if len(banned) != len(user):
                continue
            for i in range(len(user) + 1):
                if i == len(user):
                    temp.append(user)
                    break
                if banned[i] == '*':
                    continue
                if banned[i] != user[i]:
                    break
        bans[banned] = temp
        temp = []
    print(bans)
    return answer


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
