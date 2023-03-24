def solution(phone_book):
    answer = True
    nums = []
    for num in phone_book:
        nums.append([len(num), num])
    nums.sort()
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[j][1][:nums[i][0]] == nums[i][1]:
                answer = False
    return answer


print(solution(["119", "97674223", "1195524421"]))
print(solution(["12", "1235", "567", "123", "88"]))


# def solution(phone_book):
#     s = dict()
#     for p in phone_book:
#         for i in range(1, len(p)):
#             s[p[:i]] = 1
#     # s = list(s) # 주석을 풀고 제출해보세요
#     for p in phone_book:
#         if p in s:
#             return False
#     return True


# def solution(phone_book):
#     answer = True
#     hash_map = {}
#     for phone_number in phone_book:
#         hash_map[phone_number] = 1
#     for phone_number in phone_book:
#         temp = ""
#         for number in phone_number:
#             temp += number
#             if temp in hash_map and temp != phone_number:
#                 answer = False
#     return answer


# 문자열.startswith(문자열)
