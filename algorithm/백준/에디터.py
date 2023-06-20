# 리스트 2개 이용
import sys
left = list(input())   # 입력값
right = []   # 커서가 왼쪽으로 이동 시 입력값 이동
N = int(input())

for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == "L" and left:   # 커서를 왼쪽으로 옮기면
        right.append(left.pop())   # 맨 오른쪽 값을 우측 리스트로 이동
    if order[0] == "D" and right:   # 커서를 오른쪽으로 옮기면
        left.append(right.pop())   # 우측 맨 오른쪽 값(계산 상 제일 앞)을 좌측 리스트로 이동
    if order[0] == "B" and left:   # 제거 시
        left.pop()   # 좌측 리스트 마지막 값 제거(커서 이동한 만큼 우측리스트로 보내주어서)
    if order[0] == "P":   # 입력 시
        left.append(order[1])   # 좌측 리스트 마지막 자리에 입력(상동)

print("".join(left + list(reversed(right))))


# 시간 초과
# import sys
#
# input = sys.stdin.readline
# texts = list(input())
# N = int(input())
# length = len(texts)
# position = length
#
# for _ in range(N):
#     a = list(input().split())
#     if a[0] == 'L':
#         if 0 < position:
#             position -= 1
#     if a[0] == 'D':
#         if position < length:
#             position += 1
#     if a[0] == 'B':
#         if 0 < position:
#             texts = texts[0:position-1] + texts[position:]
#             position -= 1
#     if a[0] == 'P':
#         texts = texts[0:position] + [a[1]] + texts[position:]
#         position += 1
#
# print(''.join(texts))
