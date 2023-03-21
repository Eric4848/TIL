def solution(clothes):
    answer = 1
    things = {name: [] for _, name in clothes}
    for clothe, name in clothes:
        things[name].append(clothe)
    for n in things.values():
        answer *= (len(n) + 1)
    return answer - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
