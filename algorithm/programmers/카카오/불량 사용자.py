def solution(user_id, banned_id):
    is_banned = [False] * len(user_id)
    bans = {}
    temp = []
    banned_users = []
    counts = {}
    for banned in banned_id:
        banned_users.append(banned)
        if banned not in counts:
            counts[banned] = 1

        elif banned in banned_users:
            counts[banned] += 1

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
    done = []

    def search(n, check):
        nonlocal done
        if n == len(banned_users):
            check.sort()
            if check not in done:
                done.append(check[:])
            return

        for idx in range(len(user_id)):
            if is_banned[idx]:
                continue
            if user_id[idx] in bans[banned_users[n]]:
                is_banned[idx] = True
                check.append(idx)
                search(n+1, check)
                check.remove(idx)
                is_banned[idx] = False
    search(0, [])
    return len(done)


#print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
#print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
#print(solution( ["frido", "frodo"], ["fr*do", "fr**o"]))
