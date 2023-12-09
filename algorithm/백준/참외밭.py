N = int(input())
lengths = []   # 모서리들을 저장할 리스트
answer = 1   # 정답을 1로 초기화(곱하기를 하기 위해)
empty = 1   # 빈 공간을 1로 초기화
for _ in range(6):
    lengths.append(list(map(int, input().split())))
# 반시계방향으로 길이가 주어지기때문에 a, b, a, b 방식으로 반복되는 방향 중 가운데 두개가 빠진 공간이다
for i in range(6):
    if lengths[i][0] == lengths[(i+2) % 6][0] and lengths[(i+1) % 6][0] == lengths[(i+3) % 6][0]:   # 다다음 방향이 같은 것이 2번이면
        minus = [(i+1) % 6, (i+2) % 6]   # 사이 두개의 모서리가 빼는 공간
        plus = [(i-2) % 6, (i-1) % 6]   # 반복되지 않는 두개의 모서리가 넓은 공간

for num in plus:
    answer *= lengths[num][1]   # 정답에 넓은 공간의 크기를 곱한다
for num in minus:
    empty *= lengths[num][1]   # 빼는 공간에 빠지는 공간을 곱한다

answer -= empty   # 정답에서 빼는 공간을 빼준다
print(answer * N)
