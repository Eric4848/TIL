S, E = map(int, input().split())
for num in range(S, E+1):
    if num == 1:
        continue
    prime = 1
    for check in range(2, int(num**0.5)+1):
        if num % check == 0:
            prime = 0
            break
    if prime:
        print(num)
