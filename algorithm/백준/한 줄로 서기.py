N = int(input())
fronts = list(map(int, input().split()))
answers = [0 for _ in range(N)]

for i in range(N):
    cnt = 0
    for j in range(N):
        if answers[j] == 0:
            cnt += 1
        elif answers[j] <= i:
            continue
        if cnt - 1 == fronts[i]:
            answers[j] = i+1
            break

print(*answers)
