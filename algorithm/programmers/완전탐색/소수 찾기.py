from itertools import permutations


def solution(numbers):
    answer = 0
    nums = [x for x in numbers]
    dones = []
    for n in range(len(nums)):
        for a in permutations(nums, n+1):
            answer += 1
            num = a[0]
            for i in range(1, len(a)):
                num += a[i]
            num = int(num)

            if num in dones:
                answer -= 1
                continue
            else:
                dones.append(num)

            if num < 2:
                answer -= 1
                continue

            for j in range(2, num):
                if num % j == 0:
                    answer -= 1
                    break
    return answer


print(solution("17"))
print(solution("011"))
print(solution("1231"))
