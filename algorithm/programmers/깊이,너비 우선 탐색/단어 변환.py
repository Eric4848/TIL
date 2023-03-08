from collections import deque


def solution(begin, target, words):
    answer = 0
    todos = deque()
    n = len(begin)
    todos.append(begin)
    re = 0
    while todos:
        for _ in range(len(todos)):
            todo = todos.popleft()
            if todo == target:
                re = answer
                break

            for word in words:
                match = 0
                for j in range(n):
                    if word[j] == todo[j]:
                        match += 1
                if match == n-1:
                    todos.append(word)
                    words.remove(word)
        answer += 1

    return re


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))

# print(len(todo))
# if todo[0] == target:
#     return
#
# for i in range(len(words)):
#     match = 0
#     for j in range(n):
#         if todo[0][j] == words[i][j]:
#             match += 1
#     if match == 2:
#         todo.append(words[i])
