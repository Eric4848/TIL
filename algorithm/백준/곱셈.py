import sys
A, B, C = map(int, sys.stdin.readline().split())
# 시간초과
# answer = A % C
# for _ in range(B-1):
#     answer = (answer * A) % C
# print(answer)


# 나머지의 분배 법칙 => (A * B) % C = ((A % C) * (B % C)) % C
def calc(a, b):
    if b == 1:
        return a % C
    else:
        divide = calc(a, b//2)
        if b % 2 == 0:
            return (divide * divide) % C
        else:
            return (divide * divide * a) % C


print(calc(A, B))
