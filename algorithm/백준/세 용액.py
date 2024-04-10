import sys

input = sys.stdin.readline
N = int(input())
liqs = list(map(int, input().split()))
liqs.sort()   # 용액 정렬
mixed = float('inf')   # 혼합액의 농도 최대로 초기화
answers = [0, 0, 0]   # 정답 초기화

for f in range(N-2):   # 첫번째 용액 범위 처음 ~ 뒤에서 세번째
    s = f+1   # 두번째 용액은 첫번째 용액 다음
    t = N-1   # 세번째 용액은 맨 마지막 용액
    # 두, 세번째 용액을 두 포인터 탐색
    while s < t:
        mix = liqs[f] + liqs[s] + liqs[t]   # 혼합액
        # 혼합액이 정답보다 0에 가까운 경우
        if abs(mix) < mixed:
            mixed = abs(mix)   # 농도 갱신
            answers = [liqs[f], liqs[s], liqs[t]]   # 정답 용액 갱신

        # 다음 조건
        if 0 < mix:   # 혼합액이 양수인 경우
            t -= 1   # 줄여준다
        elif mix < 0:   # 혼합액이 음수인 경우
            s += 1    # 늘려준다
        else:   # 혼합액이 0이면
            break   # 종료

print(*answers)


# 시간 초과 Pypy3는 가능
# import sys
#
# input = sys.stdin.readline
# N = int(input())
# liqs = list(map(int, input().split()))
# liqs.sort()
# mixed = float('inf')
# answers = [0, 0, 0]
# for f in range(N-2):
#     s = f+1
#     t = N-1
#     while s < t:
#         mix = abs(liqs[f] + liqs[s] + liqs[t])
#         if mix < mixed:
#             mixed = mix
#             answers = [liqs[f], liqs[s], liqs[t]]
#
#         if 0 < liqs[f] + liqs[s] + liqs[t]:
#             t -= 1
#         else:
#             s += 1
#
# print(*answers)
