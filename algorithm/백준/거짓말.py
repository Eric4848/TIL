import sys

input = sys.stdin.readline
N, M = map(int, input().split())
answers = [True] * M   # 모든 파티에 갈 수 있다고 가정
knows = list(map(int, input().split()))[1:]   # 이미 아는 사람들의 리스트
comes = []   # 파티마다 참석하는 사람들의 리스트
for _ in range(M):
    comes.append(list(map(int, input().split()))[1:])

for _ in range(M-1):   # 총 파티수 -1만큼(동일한 파티의 경우 계산하지 않는다)
    for i in range(M):   # 파티별로
        for come in comes[i]:   # 파티에 참석하는 사람이
            if come in knows:   # 이미 아는사람이라면
                for new in comes[i]:   # 해당 파티의 사람들 중
                    if new not in knows:   # 모르는 사람들을
                        knows.append(new)   # 아는 사람 리스트에 추가한다
                break

for i in range(M):   # 파티별로
    for come in comes[i]:   # 참석자들 중에
        if come in knows:   # 아는 사람이 있으면
            answers[i] = False   # 그 파티는 가지 못한다
            break
print(sum(answers))
