N = int(input())
crains = list(map(int, input().split()))
crains.sort(reverse=True)   # 크레인 최대 무게를 역순으로 정렬
M = int(input())
cargos = list(map(int, input().split()))
cargos.sort(reverse=True)   # 화물 무게를 역순으로 정렬
answer = 0
crain_num = 0   # 사용할 크레인 번호
for _ in range(2 * M):   # 2 * 화물 갯수 만큼 반복(크레인 전부 둘러보고 초기화 하면 화물의 2배-1번이 필요함)
    if not cargos:   # 모든 화물을 운반했으면
        break   # 종료

    if crain_num == N:   # 모든 크레인을 사용했으면
        crain_num = 0   # 크레인 번호를 0번으로 이동

    if crain_num == 0:   # 크레인 번호가 0번이면
        answer += 1   # 운반횟수를 1추가

    for cargo in cargos:   # 화물들을 둘러보며
        if cargo <= crains[crain_num]:   # 화물의 무게가 현재 크레인 최대 무게보다 작다면
            cargos.remove(cargo)   # 해당 화물을 제거하고
            crain_num += 1   # 다음 크레인으로 이동
            break   # 종료

        if cargo == cargos[-1]:   # 모든 화물을 둘러봤는데 옮길 수 없다면
            crain_num = 0   # 크레인 번호를 0번으로 이동
            break   # 종료

if cargos:   # 화물이 남아있다면
    print(-1)   # 옮길 수 없는 경우다
else:
    print(answer)
