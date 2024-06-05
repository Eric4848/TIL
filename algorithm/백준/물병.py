N, K = map(int, input().split())
bottles = [N]   # 2의 index승 물병의 갯수 / 2의 0승 N개
answer = 0   # 정답 초기화
# 물병 합치기
while bottles[-1]:   # 최대 승수에 물병이 있다면(맨 마지막 빈 한칸을 위해)
    bottles.append(bottles[-1] // 2)   # 해당 위치 물병을 합쳐서 추가
    bottles[-2] = bottles[-2] - bottles[-1] * 2   # 이전 단계 합친만큼 제거

# 물병 추가
for i in range(len(bottles)):   # 최대 승수 만큼
    # 종료 조건
    if sum(bottles) <= K:   # 총 물병 수가 조건에 맞다면
        break   # 종료
    # 물병 추가
    if bottles[i] == 1:   # 현재 승수에 물병 1개가 있다면
        answer += 2 ** i   # 현재 승수만큼 물병을 추가하고
        bottles[i] -= 1   # 현재 물병 제거(합쳐서 올라감)
        bottles[i+1] += 1    # 다음 승수의 물병 1개 추가
    # 물병 합치기
    elif bottles[i] == 2:   # 현재 승수의 물병이 2개라면
        bottles[i] = 0   # 현재 승수를
        bottles[i+1] += 1   # 합친다
print(answer)


# N, K = map(int, input().split())
# while K < N:
#     K *= 2
# tmp = K - N
# print(tmp)
