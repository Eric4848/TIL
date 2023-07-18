first = input()
second = input()
counts = [0] * len(first)   # 첫번째 단어에 각 문자별로 최대 부분집합수를 저장할 리스트

for i in range(len(second)):   # 두번째 단어의 각 문자별로
    cnt = 0   # 현재 부분집합수를 0으로 초기화하고
    for j in range(len(first)):   # 첫번째 단어의 문자별로
        if cnt < counts[j]:   # 해당 첫째 단어의 부분집합수가 현재 문자까지의 부분집합보다 작다면
            cnt = counts[j]   # 현재 부분집합수를 그 수로 바꾸어준다
        elif second[i] == first[j]:   # 혹은 두번째 단어의 문자와 첫번째 단어의 문자가 같다면
            # elif를 사용하여 나중에 계산한 이유는 해당 단어 문자의 부분집합수가 크면서 같은경우 현재 부분집합수 + 1로 저장되기 때문
            counts[j] = cnt + 1   # 첫번째 단어 해당 위치에 현재 부분집합수+1을 저장해준다

print(max(counts))

# 중간에 겹치는 문자가 있으면 뒤에 더 긴 문자열이 있어도 적용 불가
# 반례 3정답
# VREGDFELK
# VLSKD
# first = input()
# second = input()
# L = len(first)
# counts = [0] * L
# for i in range(L):
#     start = 0
#     for j in range(i, L):
#         for k in range(start, len(second)):
#             if first[j] == second[k]:
#                 counts[i] += 1
#                 start = k + 1
#                 break
# print(max(counts))
