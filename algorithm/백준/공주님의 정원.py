import sys

input = sys.stdin.readline
N = int(input())
flowers = []   # 꽃의 피고 지는 시간을 담을 리스트
for _ in range(N):
    sm, sd, em, ed = map(int, input().split())   # 피고 지는 시간을 입력받아
    flowers.append([sm * 100 + sd, em * 100 + ed])   # 각각 달에 100을 곱한 후 더해서 저장한다(앞뒤 비교만 하면 되기 때문)

flowers.sort(key=lambda x: x[0])   # 꽃이 피는 날 기준으로 정렬한다

start = 301   # 피는 조건일
mid = 301   # 현재 가장 길게 피었다 지는 날
end = 1130   # 지는 조건일
answer = 1   # 정답을 1로 초기화(1종류의 꽃은 무조건 사용)

# 필요한 꽃의 종류 계산
for i in range(N):   # 각 꽃들 별로
    s, e = flowers[i]   # 피는날, 지는날 정보를 받아온다
    if end < mid:   # 이전 계산에서 조건을 만족했다면
        break   # 종료

    if start < s:   # 현재 꽃의 피는 날이 시작일보다 늦다면
        start = mid   # 시작일을 이전 지는 날로 변경
        answer += 1   # 정답 + 1

    if s <= start:   # 현재 꽃의 피는 날이 시작일보다 이르거나 같다면
        if mid < e:   # 현재 꽃의 지는 날이 이전 지는날 보다 큰경우
            mid = e   # 지는 날을 갱신

if end < mid:   # 지는 조건일보다 현재 지는날이 크다면
    print(answer)   # 정답 출력
else:   # 아니라면
    print(0)   # 불가능

# 301 1130
